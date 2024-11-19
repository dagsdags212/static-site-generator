from htmlnode import HTMLNode, LeafNode
from textnode import TextNode, TextType


def text_node_to_html_node(text_node: TextNode) -> HTMLNode:
    """Converts a TextNode instance into an HTML-formatted node."""
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            props = {"href": text_node.url}
            return LeafNode(tag="a", value=text_node.text, props=props)
        case TextType.IMAGE:
            props = {"src": text_node.url, "alt": text_node.text}
            return LeafNode(tag="img", value="", props=props)
        case _:
            raise ValueError("invalid TextType used in TextNode")



def main():
    text = "This is a text node"
    url = "https://www.boot.dev"
    node = TextNode(text, TextType.BOLD, url)
    print(node)

if __name__ == "__main__":
    main()
