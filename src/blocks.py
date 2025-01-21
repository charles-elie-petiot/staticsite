import re

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        if block == "":
            continue
        new_blocks.append(block.strip())
    return new_blocks

def block_to_block_type(block):
    if bool(re.search(r"^#{1,6} ", block)):
        return "Heading"
    elif bool(re.search(r"^`{3}(?!`).*(?<!`)`{3}$", block)):
        return "Code"
    lines = block.split("\n")
    if all(bool(re.search(r"^>{1}", line)) for line in lines):
        return "Quote"
    elif all(bool(re.search(r"^[*|-] ", line)) for line in lines):
        return "Unordered list"
    number = 1
    for line in lines:
        if not bool(re.search(r"^\d+\. ", line)):
            return "Paragraph"
        if line.split(".")[0] != str(number):
            return "Paragraph"
        number += 1
    return "Ordered list"