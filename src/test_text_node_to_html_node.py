import unittest
from htmlnode import LeafNode
from main import text_node_to_html_node
from textnode import TextNode, TextType


class TestTextToHTML(unittest.TestCase):
    def test_convert_invalid_format(self):
        with self.assertRaises((AttributeError, ValueError)):
            init = dict(text="", text_type=TextType.HEADER, url=None)
            TextNode(**init)

    def test_convert_text(self):
        init = dict(text="This is a normal text node", text_type=TextType.TEXT, url=None)
        text_node = TextNode(**init)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertIsNone(html_node.tag)
        self.assertIsNotNone(html_node.value, str)

    def test_convert_bold(self):
        init = dict(text="This is a bold text node", text_type=TextType.BOLD, url=None)
        text_node = TextNode(**init)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertIsNotNone(html_node.tag)
        self.assertEqual(html_node.tag,  "b")
        self.assertIsNotNone(html_node.value, str)

    def test_convert_italic(self):
        init = dict(text="This is an italic text node", text_type=TextType.ITALIC, url=None)
        text_node = TextNode(**init)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertIsNotNone(html_node.tag)
        self.assertEqual(html_node.tag,  "i")
        self.assertIsNotNone(html_node.value, str)

    def test_convert_code(self):
        init = dict(text="This is a code text node", text_type=TextType.CODE, url=None)
        text_node = TextNode(**init)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertIsNotNone(html_node.tag)
        self.assertEqual(html_node.tag,  "code")
        self.assertIsNotNone(html_node.value, str)

    def test_convert_link(self):
        init = dict(text="This is a link text node", text_type=TextType.LINK, url="https://www.google.com/")
        text_node = TextNode(**init)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag,  "a")
        self.assertIsNotNone(html_node.tag)
        self.assertIsNotNone(html_node.value)
        self.assertIsNotNone(html_node.props)
        self.assertTrue("href" in html_node.props.keys())
        for v in html_node.props.values():
            self.assertIsInstance(v, str)

    def test_convert_image(self):
        init = dict(text="This is a image text node", text_type=TextType.IMAGE, url="https://www.google.com/")
        text_node = TextNode(**init)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertIsNotNone(html_node.props)
        self.assertIsNotNone(html_node.tag)
        self.assertEqual(html_node.tag,  "img")
        self.assertEqual(html_node.value, "")
        self.assertTrue("src" in html_node.props.keys())
        self.assertTrue("alt" in html_node.props.keys())
        for v in html_node.props.values():
            self.assertIsInstance(v, str)
