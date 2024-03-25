#!/usr/bin/python3
"""
This is a script to convert a Markdown file to HTML.

Usage:
    ./markdown2html.py [input_file] [output_file]

Arguments:
    input_file: the name of the Markdown file to be converted
    output_file: the name of the output HTML file

Example:
    ./markdown2html.py README.md README.html
"""

import sys
import os
import re

if __name__ == '__main__':

    
    if len(sys.argv[1:]) != 2:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        sys.exit(1)


    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f'Missing {input_file}', file=sys.stderr)
        sys.exit(1)

    with open(input_file, encoding='utf-8') as file_1:
        html_content = []
        md_content = [line[:-1] for line in file_1.readlines()]
        for line in md_content:
            if line.startswith('#'):
                h_level = line.count('#')
                html_content.append(
                    f'<h{h_level}>{line[h_level+1:]}</h{h_level}>\n'
                )
            elif line.startswith('- '):
                html_content.append(f'<li>{line[2:]}</li>\n')
            else:
                html_content.append(line + '\n')

    
    if any('<li>' in line for line in html_content):
        html_content = ['<ul>\n'] + html_content + ['</ul>\n']

    with open(output_file, 'w', encoding='utf-8') as file_2:
        file_2.writelines(html_content)
