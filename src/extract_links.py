import re

def extract_markdown_images(text):
    alts = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return alts

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return links

