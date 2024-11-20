import unittest
from textnode import TextType
from parser_engine import *


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_node_with_code_text(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)

        n1, n2, n3 = new_nodes
        self.assertEqual(n1.text_type, TextType.TEXT)
        self.assertEqual(n2.text_type, TextType.CODE)
        self.assertEqual(n3.text_type, TextType.TEXT)

        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertListEqual(new_nodes, expected)

    def test_split_node_with_italic_text(self):
        node = TextNode("This is text with an *italic* word", TextType.ITALIC)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 3)

        n1, n2, n3 = new_nodes
        self.assertEqual(n1.text_type, TextType.TEXT)
        self.assertEqual(n2.text_type, TextType.ITALIC)
        self.assertEqual(n3.text_type, TextType.TEXT)

        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertListEqual(new_nodes, expected)

    def test_split_node_with_bold_text(self):
        node = TextNode("This is text with an **bold** word", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)

        n1, n2, n3 = new_nodes
        self.assertEqual(n1.text_type, TextType.TEXT)
        self.assertEqual(n2.text_type, TextType.BOLD)
        self.assertEqual(n3.text_type, TextType.TEXT)

        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertListEqual(new_nodes, expected)

    def test_split_node_with_multiple_formatted_strings(self):
        node = TextNode(
            "This is `text` with multiple `code` block words.", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 5)

        code_nodes = list(
            filter(lambda node: node.text_type == TextType.CODE, new_nodes)
        )
        text_nodes = list(
            filter(lambda node: node.text_type == TextType.TEXT, new_nodes)
        )
        self.assertEqual(len(code_nodes), 2)
        self.assertEqual(len(text_nodes), 3)

    def test_split_node_with_invalid_delimiter(self):
        node = TextNode("This is text with a `code block` word.", TextType.TEXT)
        with self.assertRaises(ValueError):
            new_nodes = split_nodes_delimiter([node], "*", TextType.CODE)
