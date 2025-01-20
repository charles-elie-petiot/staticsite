import unittest

from textnode import TextNode, TextType
from nodes import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq_code(self):
        node = TextNode("This is a `code` text node", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE), [TextNode('This is a ', TextType.TEXT),
                                                                             TextNode('code', TextType.CODE),
                                                                             TextNode(' text node', TextType.TEXT)])

    def test_eq_bold(self):
        node = TextNode("This is a **bold** text node", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), [TextNode('This is a ', TextType.TEXT),
                                                                             TextNode('bold', TextType.BOLD),
                                                                             TextNode(' text node', TextType.TEXT)])

    def test_eq_italic(self):
        node = TextNode("This is a *italic* text node", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "*", TextType.ITALIC), [TextNode('This is a ', TextType.TEXT),
                                                                             TextNode('italic', TextType.ITALIC),
                                                                             TextNode(' text node', TextType.TEXT)])

    def test_eq_mult(self):
        node = TextNode("This is a *italic* text node with *more than one*", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "*", TextType.ITALIC), [TextNode('This is a ', TextType.TEXT),
                                                                             TextNode('italic', TextType.ITALIC),
                                                                             TextNode(' text node with ', TextType.TEXT),
                                                                             TextNode('more than one', TextType.ITALIC)])
        
    def test_eq_mult2(self):
        node = TextNode("This is a *italic* text node with *more than one* new node", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "*", TextType.ITALIC), [TextNode('This is a ', TextType.TEXT),
                                                                             TextNode('italic', TextType.ITALIC),
                                                                             TextNode(' text node with ', TextType.TEXT),
                                                                             TextNode('more than one', TextType.ITALIC),
                                                                             TextNode(' new node', TextType.TEXT)])

if __name__ == "__main__":
    unittest.main()