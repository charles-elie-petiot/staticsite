import re

def extract_markdown_images(text):
    alts = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return alts

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return links


text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
