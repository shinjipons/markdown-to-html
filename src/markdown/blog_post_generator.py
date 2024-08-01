# Fetch the markdown file
html_lines = []

def generate_html_from_markdown():
    with open('src/markdown/about-calendars.md', 'r') as file:
        markdown_content = file.read()

        # Split the markdown content into lines
        lines = markdown_content.split('\n')

        for line in lines:
            if line.startswith('#'):
                # Headers
                header_parts = line.split(' ')
                header_level = len(header_parts[0])
                header_text = ' '.join(header_parts[1:])
                header_html = f'<h{header_level}>{header_text}</h{header_level}>'
                html_lines.append(header_html)
            elif line.startswith('- '):
                # Unordered list items
                bullet_point_text = line.strip('- ')
                bullet_point_html = f'<li>{bullet_point_text}</li>'
                html_lines.append(bullet_point_html)
            elif line.startswith('!('):
                # Media (images and videos)
                media_url = line.strip('!()[]')
                media_caption = extract_parentheses(line)
                if media_url.endswith('.mp4'):
                    # Videos, without captions for now
                    video_html = f"""<video autoplay loop><source src="{media_url}" type="video/mp4"></video>"""
                    html_lines.append(video_html)
                else:
                    # Images
                    if len(media_caption) != 0: # This media has a "caption"
                        image_html = f"""<picture><img src="{media_url}"><p class="caption">{media_caption}</p></picture>"""
                        html_lines.append(image_html)
                    else:
                        image_html = f"""<picture><img src="{media_url}"></picture>"""
                        html_lines.append(image_html)
            # elif type(line[0]) == int:
                # Numbered lists
                # numbered_list_item_html = f'<p>{line}</p>'
            else:
                if len(line) !=0:
                    # Normal text, paragraphs
                    line_html = f'<p>{line}</p>'
                    html_lines.append(line_html)
    # print(html_lines)
    for html_line in html_lines:
        replace_link(html_line)

# Utility functions
def extract_parentheses(string):
    start = string.find('(')
    if start != -1: # Check if '(' is found
        end = string.find(')', start)
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
        result += f'<a href="{link_url}">{link_text}</a>'
        result += f'<a href="{link_url}" target="_blank">{link_text}</a>' # Make links open in new tab

        # Move start to after this link
        start = close_paren + 1

    return result

test_line = "<p>I got a error message because the app-specific password you use inside of Outlook must be used with the @icloud.com adress tied to your Apple ID account. If you use the email adress that you use to sign in with your Apple ID, you will get an error! How are you supposed to know that? Well, you DON'T because neither the [Apple Support](https://support.apple.com/en-gb/guide/icloud-windows/icwa12798053/icloud) nor the [Windows support](https://support.microsoft.com/en-gb/office/add-or-manage-an-icloud-email-account-in-outlook-4aed8b3d-3c68-4743-8973-f6bd1c56e040) pages mention that anywhere.</p>"
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