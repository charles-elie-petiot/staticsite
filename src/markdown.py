from blocks import markdown_to_blocks, block_to_block_type
import re
from htmlnode import HTMLNode, ParentNode
from nodes import text_to_textnodes
from textnode import text_node_to_html_node

def markdown_to_hmtl_node(markdown):
    blocks = markdown_to_blocks(markdown)
    
    block_liste = []
    for block in blocks:
        block_type= block_to_block_type(block)
        match block_type:
            case 'Heading':
                block_liste.append(heading_to_node(block))
            case "Quote":
                block_liste.append(quote_to_node(block))
            case "Unordered list":
                block_liste.append(unordered_to_node(block))
            case "Ordered list":
                block_liste.append(ordered_to_node(block))
            case "Code":
                block_liste.append(code_to_node(block))
            case "Paragraph":
                block_liste.append(parag_to_node(block))

    return ParentNode("div", block_liste)

def heading_to_node(block):
    count = len(block) - len(block.lstrip("#"))
    children = text_to_children(block.lstrip("#"))
    return ParentNode(f"h{count}", children)

def quote_to_node(block):
    text = block.replace(">", '').replace('\n', '')
    children = text_to_children(text)
    return ParentNode("blockquote", children)

def unordered_to_node(block):
    children_liste = []
    lines = block.split("\n")
    for line in lines:
        children = text_to_children(line[2:])
        children_liste.append(ParentNode("li", children))
    return ParentNode("ul", children_liste)

def ordered_to_node(block):
    children_liste = []
    lines = block.split("\n")
    for line in lines:
        sections = line.split('.')
        kept_sections = ".".join(sections[1:])
        children = text_to_children(kept_sections)
        children_liste.append(ParentNode("li", children))
    return ParentNode("ol", children_liste)

def code_to_node(block):
    children = text_to_children(block[3:-3])
    return ParentNode("pre", [ParentNode("code", children)])

def parag_to_node(block):
    children = text_to_children(block)
    return ParentNode("p", children)

def text_to_children(text):
    liste = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        liste.append(text_node_to_html_node(text_node))
    return liste
