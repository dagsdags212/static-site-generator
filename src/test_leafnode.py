import unittest
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_node_has_no_children(self):
        leaf = LeafNode("p", "This is a leaf node")
        self.assertIsNone(leaf.children)

    def test_node_without_value(self):
        with self.assertRaises((TypeError, ValueError)):
            leaf = LeafNode("a")

    def test_to_html_method(self):
        attributes = dict(value="Click me!", props={"href": "https://www.google.com"})
        # node without tag should return raw value as text
        leaf_without_tag = LeafNode(tag=None, **attributes)
        self.assertEqual(leaf_without_tag.to_html(), leaf_without_tag.value)

        # node with tag should return a formatted HTML tag
        leaf_with_tag = LeafNode(tag="a", **attributes)
        self.assertIsInstance(leaf_with_tag.to_html(), str)
        self.assertEqual(
            leaf_with_tag.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )
