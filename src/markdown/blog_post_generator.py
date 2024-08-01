html_lines = []

def generate_html_from_markdown():
    with open('src/markdown/about-calendars.md', 'r') as file:
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
                header_html = f'<h{header_level}>{header_text}</h{header_level}>'
                html_lines.append(header_html)
            elif line.startswith('- '): # Unordered list items
                bullet_point_text = line.strip('- ')
                bullet_point_html = f'<li>{bullet_point_text}</li>'
                html_lines.append(bullet_point_html)
            elif line.startswith('!('): # Media (images and videos)
                media_caption = extract_parentheses(line)
                media_url = extract_brackets(line)
                if media_url.endswith('.mp4'): # Videos, without captions for now
                    video_html = f"""<video autoplay loop><source src="{media_url}" type="video/mp4"></video>"""
                    html_lines.append(video_html)
                elif len(media_caption) == 0: # image without caption
                    image_html = f"""<picture><img src="{media_url}"></picture>"""
                    html_lines.append(image_html)
                else: # image with caption
                    image_html = f"""<picture><img src="{media_url}"><p class="caption">{media_caption}</p></picture>"""
                    html_lines.append(image_html)
            elif line.startswith(("1", "2", "3", "4", "5", "6", "7", "8", "9")): # Numbered lists (ugly but works)
                numbered_list_item_html = f'<li>{line}</li>'
            elif line.startswith('> '): # Quotes
                quote_text = line.lstrip("> ")
                quote_html = f"""<div class="blog-quote"><p>{quote_text}</p></div>"""
                html_lines.append(quote_html)
            else: # Normal text paragraphs
                line_html = f'<p>{line}</p>'
                html_lines.append(line_html)

    for html_line in html_lines:
        html_line = replace_bold(html_line)
        html_line = replace_link(html_line)

    # for html_line in html_lines: # For testing only!
    #     print(html_line)

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

# Generate some simple ass shit HTML from it
generate_html_from_markdown()
# print(generate_html_from_markdown())

# todo
# front matter support
# <ul> and <ol> wrapper support
# code block support

# done