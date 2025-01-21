import unittest

from textnode import TextNode, TextType
from nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes


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
        
    def test_split_error(self):
        node = TextNode("This is a *italic* text node with *more than", TextType.TEXT)

        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(str(context.exception), 'Invalid markdown')

    def test_split_image(self):
        node = TextNode(
            "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev) test",
            TextType.TEXT,      
        )
        self.assertEqual(split_nodes_image([node]), [TextNode('This is text with a link ' , TextType.TEXT),
                                                     TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'),
                                                     TextNode(' and ' , TextType.TEXT),
                                                     TextNode('to youtube', TextType.IMAGE, 'https://www.youtube.com/@bootdotdev'),
                                                     TextNode(' test' , TextType.TEXT)])
        
    def test_split_image2(self):
        node = TextNode(
            "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,      
        )
        self.assertEqual(split_nodes_image([node]), [TextNode('This is text with a link ' , TextType.TEXT),
                                                     TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'),
                                                     TextNode(' and ' , TextType.TEXT),
                                                     TextNode('to youtube', TextType.IMAGE, 'https://www.youtube.com/@bootdotdev'),])

    def test_split_image3(self):
        node = TextNode(
            "![to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,      
        )
        self.assertEqual(split_nodes_image([node]), [TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'),
                                                     TextNode(' and [to youtube](https://www.youtube.com/@bootdotdev)' , TextType.TEXT),])
        
    def test_split_links(self):
        node = TextNode(
            "![to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,      
        )
        self.assertEqual(split_nodes_link([node]), [TextNode('![to boot dev](https://www.boot.dev) and ', TextType.TEXT),
                                                    TextNode('to youtube', TextType.LINK, 'https://www.youtube.com/@bootdotdev')])
        
    def test_split_links2(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,      
        )
        self.assertEqual(split_nodes_link([node]), [TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'),
                                                    TextNode(' and ', TextType.TEXT),
                                                    TextNode('to youtube', TextType.LINK, 'https://www.youtube.com/@bootdotdev')])
        
    def test_split_links_nolinks(self):
        node = TextNode(
            "![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,      
        )
        self.assertEqual(split_nodes_link([node]), [TextNode('![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)', TextType.TEXT)])

    def test_text_to_nodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertEqual(text_to_textnodes(text), [TextNode("This is ", TextType.TEXT),
                                                   TextNode("text", TextType.BOLD),
                                                   TextNode(" with an ", TextType.TEXT),
                                                   TextNode("italic", TextType.ITALIC),
                                                   TextNode(" word and a ", TextType.TEXT),
                                                   TextNode("code block", TextType.CODE),
                                                   TextNode(" and an ", TextType.TEXT),
                                                   TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                                                   TextNode(" and a ", TextType.TEXT),
                                                   TextNode("link", TextType.LINK, "https://boot.dev"),
                                                   ])
if __name__ == "__main__":
    unittest.main()