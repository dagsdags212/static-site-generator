import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("Node 1", TextType.BOLD, None)
        node2 = TextNode("Node 2", TextType.BOLD, "https://www.boot.dev/")
        self.assertNotEqual(node, node2)

    def test_missing_url(self):
        node = TextNode("Node without a url", TextType.BOLD)
        self.assertIs(node.url, None)

    def test_invalid_text_type(self):
        with self.assertRaises(AttributeError):
            node = TextNode("Node without invalid TextType", TextType.BLUE)

    def test_missing_text_type(self):
        with self.assertRaises((TypeError, AttributeError)):
            node = TextNode("Node without invalid TextType", TextType.BLUE)


if __name__ == "__main__":
    unittest.main()
