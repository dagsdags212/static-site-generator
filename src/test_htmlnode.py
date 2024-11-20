import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_empty_html_node(self):
        """Returns a valid HTMLNode object with empty attributes."""
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_props_to_html_method(self):
        attributes = dict(
            tag="p",
            value="parent",
            children=[],
            props={"style": "color: green;"},
        )
        node = HTMLNode(**attributes)
        props_str = node.props_to_html()
        self.assertIsInstance(props_str, str)
        self.assertEqual(props_str, ' style="color: green;"')

    def test_repr(self):
        attributes = dict(
            tag="a",
            value=None,
            children=[],
            props={"style": "color: green;", "url": "https://www.boot.dev"},
        )
        node = HTMLNode(**attributes)
        self.assertIsInstance(node.__repr__(), str)
        self.assertTrue(node.__repr__().startswith("HTMLNode"))
