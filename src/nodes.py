from textnode import TextNode, TextType
from extract_links import extract_markdown_images, extract_markdown_links

node = TextNode("This is text with a `code block` word", TextType.TEXT)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    liste = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            liste.append(old_node)
            continue

        new_nodes = old_node.text.split(delimiter)
        if len(new_nodes) % 2 == 0:
            raise Exception('Invalid markdown')
        for i in range(len(new_nodes)):
            if new_nodes[i] == "":
                continue
            if i % 2 == 0:
                liste.append(TextNode(new_nodes[i], TextType.TEXT))
            else :
                liste.append(TextNode(new_nodes[i], text_type))
    
    return liste

def split_nodes_image(old_nodes):
    liste = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            liste.append(old_node)
            continue
        new_text = old_node.text
        images = extract_markdown_images(new_text)
        if images == []:
            liste.append(old_node)
            continue
        for image in images:
            new_text = new_text.replace(f"![{image[0]}]({image[1]})", "img")
        new_nodes = new_text.split("img")
        for i in range(len(new_nodes) -1):
            if new_nodes[i] == "":
                liste.append(TextNode(images[i][0], TextType.IMAGE, images[i][1]))
                continue
            liste.append(TextNode(new_nodes[i], TextType.TEXT))
            liste.append(TextNode(images[i][0], TextType.IMAGE, images[i][1]))
        if new_nodes[-1] == "":
            continue
        else:
            liste.append(TextNode(new_nodes[-1], TextType.TEXT))
    return liste

def split_nodes_link(old_nodes):
    liste = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            liste.append(old_node)
            continue
        new_text = old_node.text
        links = extract_markdown_links(new_text)
        if links == []:
            liste.append(old_node)
            continue
        for link in links:
            new_text = new_text.replace(f"[{link[0]}]({link[1]})", "lnk")
        new_nodes = new_text.split("lnk")
        for i in range(len(new_nodes) -1):
            if new_nodes[i] == "":
                liste.append(TextNode(links[i][0], TextType.LINK, links[i][1]))
                continue
            liste.append(TextNode(new_nodes[i], TextType.TEXT))
            liste.append(TextNode(links[i][0], TextType.LINK, links[i][1]))
        if new_nodes[-1] == "":
            continue
        else:
            liste.append(TextNode(new_nodes[-1], TextType.TEXT))
    return liste

def text_to_textnodes(text):
    liste = [TextNode(text, TextType.TEXT)]
    liste = split_nodes_delimiter(liste, "`", TextType.CODE)
    liste = split_nodes_delimiter(liste, "**", TextType.BOLD)
    liste = split_nodes_delimiter(liste, "*", TextType.ITALIC)
    liste = split_nodes_image(liste)
    liste = split_nodes_link(liste)


    return liste

test = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

