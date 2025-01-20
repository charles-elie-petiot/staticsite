import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
            
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("p", "test", [], props)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_no_props_to_html(self):
            
        props = {}
        node = HTMLNode("p", "test", [])
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html2(self):
            
        props = {        
            "href": "https://www.google.com",
            "target": "_blank",
            "object": "test3"
        }
        node = HTMLNode("p", "test", [], props)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank" object="test3"')

    def test_leafnode(self):
        props = {}
        node = LeafNode('p', 'This is a paragraph')
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")

    def test_leafnode_props(self):
        props = {        
            "href": "https://www.google.com"
        }
        node = LeafNode('p', 'This is a paragraph', props)
        self.assertEqual(node.to_html(), '<p href="https://www.google.com">This is a paragraph</p>')

    def test_leafnode_props2(self):
        props = {        
            "href": "https://www.google.com",
            "target": "_blank",
            "object": "test3"
        }
        node = LeafNode('p', 'This is a paragraph', props)
        self.assertEqual(node.to_html(), '<p href="https://www.google.com" target="_blank" object="test3">This is a paragraph</p>')

    def test_parentnode(self):
        props={}
        children=[LeafNode('b', 'I am the child')]

        node = ParentNode('p', children)
        self.assertEqual(node.to_html(), "<p><b>I am the child</b></p>")

    def test_parentnode_props(self):
        props={"target": "_blank"}
        children=[LeafNode('b', 'I am the child')]

        node = ParentNode('p', children, props)
        self.assertEqual(node.to_html(), '<p target="_blank"><b>I am the child</b></p>')

    def test_multiple_parent(self):
        props={"target": "_blank"}
        children=[LeafNode('b', 'I am the child'),
                  LeafNode('a', 'here is a link')]

        node = ParentNode('p', children, props)
        self.assertEqual(node.to_html(), '<p target="_blank"><b>I am the child</b><a>here is a link</a></p>')

    def test_no_children_error(self):
        props={"target": "_blank"}
        children=[LeafNode('b', 'I am the child'),
                  LeafNode('a', 'here is a link')]

        node = ParentNode('p', None, props)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "Missing children")

    def test_no_tag_error(self):
        props={"target": "_blank"}
        children=[LeafNode('b', 'I am the child'),
                  LeafNode('a', 'here is a link')]

        node = ParentNode(None, children, props)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "No tag")


    def test_nested_parent(self):
        props={"target": "_blank"}
        children=[LeafNode('b', 'I am the child'),
                  ParentNode('h1', [LeafNode('h2', 'firstborn'),
                                    LeafNode('h3', 'secondborn', {"object": "test3"})])]

        node = ParentNode('p', children, props)
        self.assertEqual(node.to_html(), '<p target="_blank"><b>I am the child</b><h1><h2>firstborn</h2><h3 object="test3">secondborn</h3></h1></p>')

if __name__ == "__main__":
    unittest.main()