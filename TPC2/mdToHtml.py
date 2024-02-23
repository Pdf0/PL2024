import sys
import re

def buildh(match_object):
    n = len(match_object.group(1))
    return f"<h{n}>" + match_object.group(2) + f"</h{n}>"

def buildUl(match_object):
    return "<ul>\n" + buildIl(match_object.group(1), "ul") + "</ul>\n"

def buildOl(match_object):
    return "<ol>\n" + buildIl(match_object.group(1), "ol") + "</ol>\n"

def buildIl(match_object, listType):
    if listType == "ul":
        r = re.sub(r'((\s*)?-\s+.*)', r'<li>\1</li>\n', match_object)
        r = re.sub(r'(- |\n)', '', r)
        r = re.sub(r'</li>', '</li>\n', r)
    elif listType == "ol":
        r = re.sub(r'((\s*)?\d+\.\s+.*)', r'<li>\1</li>\n', match_object)
        r = re.sub(r'(\d+\. |\n)', '', r)
        r = re.sub(r'</li>', '</li>\n', r)
    else:
        return match_object
    return r

def main(args):
    if len(args) != 3:
        print("Usage: python mdToHtml.py <input_file> <output_file>")
        sys.exit(1)

    input_file = args[1]

    try:
        with open(input_file, 'r') as file:
            data = file.read()
            # headers
            data = re.sub(r'(#+)(.*)', buildh, data)
            # bold
            data = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', data)
            # italic
            data = re.sub(r'\*(.*)\*', r'<i>\1</i>', data)       
            # unordered lists
            data = re.sub(r'^(\s*-\s+.*(?:\n\s*-\s+.*)*)+', buildUl, data, flags=re.MULTILINE)
            # ordered lists
            data = re.sub(r'^(\s*\d+\.\s+.*(?:\n\s*\d+\.\s+.*)*)+', buildOl, data, flags=re.MULTILINE)
            # images
            data = re.sub(r'\!\[(.*)\]\((.*)\)', r'<img src="\2" alt="\1"/>', data)
            # links
            data = re.sub(r'\[(.*)\]\((.*)\)', r'<a href="\2">\1</a>', data)
            # 

            print(data)                

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
        sys.exit(2)

if __name__ == '__main__':
    main(sys.argv)