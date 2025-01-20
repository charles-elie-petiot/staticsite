import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, url = None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("this is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_equal_text_type(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_equal_url(self):
        node = TextNode("This is a text node", TextType.BOLD, url ='http')
        node2 = TextNode("this is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_leafnode_text(self):
        node = TextNode("this is a text node", TextType.TEXT)
        self.assertEqual(text_node_to_html_node(node).to_html(), "this is a text node")

    def test_leafnode_bold(self):
        node = TextNode("this is a text node", TextType.BOLD)
        self.assertEqual(text_node_to_html_node(node).to_html(), "<b>this is a text node</b>")

    def test_leafnode_italic(self):
        node = TextNode("this is a text node", TextType.ITALIC)
        self.assertEqual(text_node_to_html_node(node).to_html(), "<i>this is a text node</i>")

    def test_leafnode_code(self):
        node = TextNode("this is a text node", TextType.CODE)
        self.assertEqual(text_node_to_html_node(node).to_html(), "<code>this is a text node</code>")

    def test_leafnode_link(self):
        node = TextNode("this is a text node", TextType.LINK, 'http://link')
        self.assertEqual(text_node_to_html_node(node).to_html(), '<a href="http://link">this is a text node</a>')

    def test_leafnode_image(self):
        node = TextNode("text node", TextType.IMAGE, 'http://link')
        self.assertEqual(text_node_to_html_node(node).to_html(), '<img src="http://link" alt="text node"></img>')

if __name__ == "__main__":
    unittest.main()