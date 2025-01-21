import unittest

from blocks import markdown_to_blocks, block_to_block_type


class TestBlocks(unittest.TestCase):
    def test_blocks(self):
        markdown = """# This is a heading

 This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        self.assertEqual(markdown_to_blocks(markdown), ['# This is a heading',
                                                        'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
                                                        '* This is the first list item in a list block\n* This is a list item\n* This is another list item'])
        

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph


This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_heading(self):
        md = "### heading"
        self.assertEqual(block_to_block_type(md), "Heading")

    def test_heading2(self):
        md = " ### heading"
        self.assertEqual(block_to_block_type(md), "Paragraph")

    def test_heading3(self):
        md = "####### heading"
        self.assertEqual(block_to_block_type(md), "Paragraph")

    def test_code(self):
        md = "``` heading ```"
        self.assertEqual(block_to_block_type(md), "Code")

    def test_code2(self):
        md = "``` heading ````"
        self.assertEqual(block_to_block_type(md), "Paragraph")

    def test_code3(self):
        md = "`` heading ```"
        self.assertEqual(block_to_block_type(md), "Paragraph")

    def test_quote(self):
        md = """> quote 
> next
> next"""
        self.assertEqual(block_to_block_type(md), "Quote")

    def test_quote2(self):
        md = """> quote 
 > next
> next"""
        self.assertEqual(block_to_block_type(md), "Paragraph")

    def test_ul(self):
        md = """* ul 
* next
* next"""
        self.assertEqual(block_to_block_type(md), "Unordered list")

    def test_ul2(self):
        md = """* ul 
*next
* next"""
        self.assertEqual(block_to_block_type(md), "Paragraph")

    def test_ol(self):
        md = """1. ul 
2. next
3. next"""
        self.assertEqual(block_to_block_type(md), "Ordered list")

    def test_ol2(self):
        md = """1. ul 
2.next
3. next"""
        self.assertEqual(block_to_block_type(md), "Paragraph")


if __name__ == "__main__":
    unittest.main()