from textnode import TextNode, TextType

node = TextNode("This is text with a `code block` word", TextType.TEXT)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    liste = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            liste.append(old_node)

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