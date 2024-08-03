import os

# Set the output folder
OUTPUT_FOLDER = 'dist/blog'

# Create the output folder if it doesn't exist
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

html_lines = []
ul_list_item_class = "bullet-point-list-item"
ol_list_item_class = "numbered-list-item"
code_block_class = "blog-code-block"

# Main function thath does the magic
def generate_html_from_markdown(markdown_filepath):

    with open(markdown_filepath, 'r') as file:
        markdown_content = file.read()

        # Split the markdown content into lines
        lines = markdown_content.split('\n')

        for line in lines:
            if len(line) == 0 or line.startswith(("---", "date:", "title:", "author:")): # Empty lines and front matter
                pass
            elif line.startswith('#'): # Headers
                header_parts = line.split(' ')
                header_level = len(header_parts[0])
                header_text = ' '.join(header_parts[1:])
                header_html = f'<h{header_level}>{header_text}</h{header_level}>' # need to add the ids? or do it via javascript
                html_lines.append(header_html)
            elif line.startswith('- '): # Unordered list items
                bullet_point_text = line.strip('- ')
                bullet_point_html = f"""\t<li class="{ul_list_item_class}">{bullet_point_text}</li>"""
                html_lines.append(bullet_point_html)
            elif line.startswith(("1", "2", "3", "4", "5", "6", "7", "8", "9")): # Ordered lists (ugly but works)
                numbered_list_item_parts = line.split(". ")
                numbered_list_item_text = ' '.join(numbered_list_item_parts[1:])
                numbered_list_item_html = f"""\t<li class="{ol_list_item_class}">{numbered_list_item_text}</li>"""
                html_lines.append(numbered_list_item_html)
            elif line.startswith('!('): # Media (images and videos)
                media_caption = extract_parentheses(line)
                media_url = extract_brackets(line)
                if media_url.endswith('.mp4'): # Videos, without captions for now
                    video_html = f"""<video autoplay loop><source src="{media_url}" type="video/mp4" /></video>"""
                    html_lines.append(video_html)
                elif len(media_caption) == 0: # image without caption
                    image_html = f"""<picture><img src="{media_url}"></picture>"""
                    html_lines.append(image_html)
                else: # image with caption
                    image_html = f"""<picture><img src="{media_url}"><p class="caption">{media_caption}</p></picture>"""
                    html_lines.append(image_html)
            elif line.startswith('> '): # Quotes
                quote_text = line.lstrip("> ")
                quote_html = f"""<div class="blog-quote"><p>{quote_text}</p></div>"""
                html_lines.append(quote_html)
            else: # Normal text paragraphs
                line_html = f"""<p>{line}</p>"""
                html_lines.append(line_html)

    return html_lines

# Utility functions
def extract_parentheses(string):
    start = string.find('(')
    if start != -1: # Check if '(' is found
        end = string.find(')', start)
        if end != -1: # Check if ')' is found
            return string[start + 1 : end]
    return None # Return None if parentheses are not found

def extract_brackets(string):
    start = string.find('[')
    if start != -1: # Check if '(' is found
        end = string.find(']', start)
        if end != -1: # Check if ')' is found
            return string[start + 1 : end]
    return None # Return None if parentheses are not found

def replace_link(text):
    start = 0
    result = ""
    while True:
        # Find the next markdown link
        open_bracket = text.find('[', start)
        if open_bracket == -1:
            result += text[start:]
            break

        close_bracket = text.find(']', open_bracket)
        open_paren = text.find('(', close_bracket)
        close_paren = text.find(')', open_paren)

        if -1 in (close_bracket, open_paren, close_paren):
            result += text[start:]
            break

        # Extract link text and URL
        link_text = text[open_bracket + 1:close_bracket]
        link_url = text[open_paren + 1:close_paren]

        # Add text before the link and the converted link
        result += text[start:open_bracket]
        result += f'<a href="{link_url}" target="_blank">{link_text}</a>' # Make links open in new tab

        # Move start to after this link
        start = close_paren + 1
    return result

def replace_bold(text):
    i = 0
    result = ""
    while i < len(text):
        if text[i:i+2] == '**':
            j = i + 2
            while j < len(text) and text[j:j+2] != '**':
                j += 1
            if j < len(text):
                # Add <b> and </b> around the bold text
                result += '<b>' + text[i+2:j] + '</b>'
                i = j + 2
            else:
                result += text[i:]
                break
        else:
            result += text[i]
            i += 1
    return result

def wrap_list_with_prefix(input_list, prefix, opening_html_tag):
    def create_after_item(item):
        return item[:1] + "/" + item[1:]

    result = input_list.copy()
    i = 0
    while i < len(result):
        if result[i].startswith(prefix):
            # Find the end of the contiguous block
            j = i + 1
            while j < len(result) and result[j].startswith(prefix):
                j += 1

            # Insert items before and after the block
            result.insert(i, opening_html_tag)
            result.insert(j + 1, create_after_item(opening_html_tag))

            # Move the index past the block and new items
            i = j + 2
        else:
            i += 1

    return result

# Replace the bold ** with <b> tags
html_lines_b = []
for line in generate_html_from_markdown("src/markdown/about-calendars.md"):
    if "**" in line:
        html_lines_b.append(replace_bold(line))
    else:
        html_lines_b.append(line)

# Replace the ()[] with <a> tags
html_lines_b_a = []
for line in html_lines_b:
    if "](" in line:
        html_lines_b_a.append(replace_link(line))
    else:
        html_lines_b_a.append(line)

# Wrapping the numbered and unordered list needs to happens outside of the main function, because they need to have "visibility" over the whole list
html_lines_b_a_ul = wrap_list_with_prefix(html_lines_b_a, f"\t<li class=\"{ul_list_item_class}\">", "<ul>")
html_lines_b_a_ul_ol = wrap_list_with_prefix(html_lines_b_a_ul, f"\t<li class=\"{ol_list_item_class}\">", "<ol>")

# Now deal with the code block
html_lines_b_a_ul_ol_code = [] # Finished code!
count = 0
for line in html_lines_b_a_ul_ol:
    if line.lower() == "<p>```</p>":
        if count % 2 == 0: # it's an opening tag
            new_line = f"""<div class=\"{code_block_class}\">"""
            html_lines_b_a_ul_ol_code.append(new_line)
            count += 1
        else: # it's a closing tag
            new_line = f"""</div>"""
            html_lines_b_a_ul_ol_code.append(new_line)
            count += 1
    else: # don't do anything
        html_lines_b_a_ul_ol_code.append(line)

# Generate the post title
def get_post_title(markdown_filepath):
    post_title = ""

    with open(markdown_filepath, 'r') as file:
        markdown_content = file.read()
    lines = markdown_content.split('\n')

    for line in lines:
        if line.startswith("title: "):
            post_title = line.split("title: ", 1)[-1]

    return post_title

def generate_page(post_title, post_description, html_lines):
    new_line = "\n"
    html_template = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1">
        <title>Shinji Pons | Product Designer of 3D Tools & Beyond | {post_title}</title>
        <meta name="description"          content="{post_description}">
        <link rel="stylesheet" href="css/styles.css">
        <meta property="og:url"           content="https://shinjipons.com">
        <meta property="og:type"          content="website">
        <meta property="og:title"         content="Shinji Pons | Product Designer of 3D Tools & Beyond | {post_title}">
        <meta property="og:description"   content="{post_description}">
        <meta property="og:image"         content="https://www.shinjipons.com/images/opengraph.jpg">
        <meta name="twitter:card"         content="summary_large_image">
        <meta property="twitter:domain"   content="shinjipons.com">
        <meta property="twitter:url"      content="https://shinjipons.com">
        <meta name="twitter:title"        content="Shinji Pons | Product Designer of 3D Tools & Beyond | {post_title}">
        <meta name="twitter:description"  content="{post_description}">
        <meta name="twitter:image"        content="https://www.shinjipons.com/images/opengraph.jpg">
        <link rel="icon" type="image/png" sizes="32x32"   href="/icons/favicon-32x32.png">
        <link rel="icon" type="image/png" sizes="16x16"   href="/icons/favicon-16x16.png">
        <link rel="apple-touch-icon"      sizes="180x180" href="/icons/favicon-ios.png">
    </head>
    <body>
        <main>
            <div class="left-column">
                <ul class="monospace padding-between-items">Outline
                </ul>
            </div>
            <div class="right-column">
                {f"{new_line.join(html_lines)}"}
            </div>
        </main>
        <script type="text/javascript" src="js/script.js"></script>
    </body>
    </html>
    """
    post_filename = post_title.strip("\"").replace(" ", "-").lower()
    output_path = os.path.join(OUTPUT_FOLDER, f"{post_filename}.html")

    with open(output_path, "w") as html_file:
        html_file.write(html_template)

# Generate a single page
generate_page(get_post_title("src/markdown/about-calendars.md"), "This is a test description.",  html_lines_b_a_ul_ol_code)

# todo
# get it to loop over all the markdown files inside of a directory

# done
# write the html to the dist folder with the right file name

# maybe
# think about generating the paths for the images and videos programmatically