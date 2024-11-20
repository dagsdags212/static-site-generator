import unittest
from htmlnode import LeafNode, ParentNode


class TestParentNode(unittest.TestCase):
    def test_node_without_tag(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]
        with self.assertRaises((AttributeError, TypeError)):
            ParentNode(children=children)

    def test_node_without_children(self):
        with self.assertRaises((AttributeError, TypeError)):
            ParentNode(tag="div")

    def test_to_html_method_with_two_levels(self):
        parent = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        html = parent.to_html()
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(html, expected)

    def test_to_html_method_with_three_levels(self):
        root = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode("i", "italic text"),
                ParentNode(
                    "div", [LeafNode(None, "Normal text"), LeafNode("p", "Paragraph")]
                ),
                LeafNode(None, "Normal text"),
            ],
        )
        html = root.to_html()
        expected = "<p><b>Bold text</b><i>italic text</i><div>Normal text<p>Paragraph</p></div>Normal text</p>"
        self.assertEqual(html, expected)
