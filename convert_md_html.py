"""
This script will take a blog post in markdown format and convert it to HTML.
* Once it's in HTML, we will then add anchor links to headers: <a href=#header"><h1 id="header">Header</h1></a>
* It should then prettify the HTML and write this to another file.
"""
import os
import markdown
from bs4 import BeautifulSoup
import re

github_repo = 'website_assets'


def convert_markdown_to_html(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        markdown_text = file.read()

    # Convert Markdown to HTML with tables and code highlighting extensions
    html_content = markdown.markdown(markdown_text, extensions=['tables', 'markdown.extensions.codehilite'])

    soup = BeautifulSoup(html_content, 'html.parser')

    # Add CSS class to table
    for table in soup.find_all('table'):
        table['class'] = 'page-table'

    # Add anchor links to h1, h2, h3.
    for header in soup.find_all(re.compile(r'^h[1-3]$')):
        anchor_link_id = header.text.lower().strip()
        anchor_link_id = anchor_link_id.replace(' ', '-')
        for character_to_remove in ['.', '(', ')', '?']:
            anchor_link_id = anchor_link_id.replace(character_to_remove, '')
        anchor_tag = soup.new_tag('a',
                                  id=anchor_link_id,
                                  href=f'#{anchor_link_id}',
                                  title='Permalink',
                                  **{'class': 'anchor-link', 'aria-hidden': 'true'},
                                  )
        anchor_tag.string = '#'  # This will be the text for the anchor link
        header.insert(0, anchor_tag)  # Insert the anchor tag at the beginning of the header

# Update all the images
    # This converts rel and abs path into rel path
    directory = os.path.dirname(input_file)
    directory_parts = directory.split('/')
    index = 0
    for directory_part in directory_parts:
        if directory_part == github_repo:
            directory = '/'.join(directory_parts[index + 1:])
            break
        index += 1

    for img in soup.find_all('img'):
        original_src = img['src']
        # Following: https://gist.github.com/jcubic/a8b8c979d200ffde13cc08505f7a6436
        img['src'] = f"https://cdn.jsdelivr.net/gh/artie-labs/website_assets/{directory}/{original_src}"
    return str(soup)


def write_html_to_file(html_content, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_content)


def convert_markdown_to_html_with_anchors(input_file, output_file):
    html_content = convert_markdown_to_html(input_file)
    write_html_to_file(html_content, output_file)


if __name__ == "__main__":
    file_to_convert = input("Enter the path to the markdown file: ")

    if not os.path.isabs(file_to_convert):
        file_to_convert = os.path.abspath(file_to_convert)

    input_file_name, input_file_extension = os.path.splitext(os.path.basename(file_to_convert))
    output_file_name = f"{input_file_name}_with_anchors.html"
    output_file = os.path.join(os.path.dirname(file_to_convert), output_file_name)

    convert_markdown_to_html_with_anchors(file_to_convert, output_file)
