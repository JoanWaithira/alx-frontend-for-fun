import sys
import os
import markdown

def convert_markdown_to_html(markdown_file, output_file):
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)
        
    with open(markdown_file, 'r') as md_file:
        markdown_content = md_file.read()
        html_content = markdown.markdown(markdown_content)

    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(markdown_file, output_file)
    
    sys.exit(0)