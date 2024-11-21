import re
from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    """Dissects a list of TextNode objects into a new list of atomic TextNodes


    Parameters
    ----------
    old_nodes : list[TextNode]
        A list of TextNode objects that will be split into component TextNodes
    delimiter : str
        A single-character string used to split the TextNode text
    text_type : TextType
        An enum that specifies the kind of Markdown formatter used

    Returns
    ------
    list[TextNode]
        A 2D list of TextNode objects where each row represents a parent node and
        each column points to a child node
    """
    new_nodes = []
    for node in old_nodes:
        # append the same node if delimiter is not in text
        if delimiter not in node.text:
            raise ValueError("delimiter was not used in the node text")

        children = []
        tokens = node.text.split(delimiter)
        # formatted text node occurs every other element in the list
        for token_idx in range(1, len(tokens), 2):
            children.append(TextNode(tokens[token_idx - 1], TextType.TEXT))
            children.append(TextNode(tokens[token_idx], text_type))
        # add the final node to the list
        children.append(TextNode(tokens[-1], TextType.TEXT))
        new_nodes.extend(children)

    return new_nodes


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    """Extracts the alt-text and url properties from a Markdown-formatted
    string

    Parameters
    ----------
    text : str
        A Markdown-formatted string with may or may not contain images

    Returns
    -------
        A list of 2-element tuples where each tuple follows the format:
        (alt-text, url)
    """
    img_re = r"!\[([\w\s]*)\]\(([\w\s:\/\.]+)\)"
    return re.findall(img_re, text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    """Extracts the fig-cap and url properties from a Markdown-formatted
    string

    Parameters
    ----------
    text : str
        A Markdown-formatted string with may or may not contain links

    Returns
    -------
        A list of 2-element tuples where each tuple follows the format:
        (fig-cap, url)
    """
    link_re = r"(?<!!)\[([\w\s]*)\]\(([\w\s:\/\.]+)\)"
    return re.findall(link_re, text)


def split_nodes_image(old_nodes: list[TextNode]) -> list[list[TextNode]]:
    """Splits a list of TextNode objects into its text and image components

    A Markdown-formatted image contains two data attributes: (1) an alt-text
    which is rendered when the image failed to load and a (2) url which point
    to where the image is stored

    Parameters
    ----------
    old_nodes : list[TextNode]
        A list of TextNode objects containing markdown-formatted images

    Returns
    -------
    list[TextNode]
        A new list of TextNode objects where the alt-text and url components
        have been separated
    """

    def split_single_node_image(node: TextNode) -> list[TextNode]:
        """A helper function that operates on a single node."""

        new_nodes = []
        img_re = r"(?<=!)\[([^\[\]]*)\]\((.*?)\)"
        tokens = re.split(img_re, node.text)
        for i in range(0, len(tokens) - 1, 3):
            text, caption, url = tokens[i : i + 3]
            text = text.replace("!", "")
            new_nodes.append(TextNode(text, TextType.TEXT))
            new_nodes.append(TextNode(caption, TextType.IMAGE, url))
        return new_nodes

    return list(map(split_single_node_image, old_nodes))


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    """Splits a list of TextNode objects into its text and link components

    A Markdown-formatted link contains two data attributes: a highlighted
    text and a url. When clicked, the highlighted text redirects to the url

    Parameters
    ----------
    old_nodes : list[TextNode]
        A list of TextNode objects containing markdown-formatted links

    Returns
    -------
    list[TextNode]
        A new list of TextNode objects where the fig-cap and url components
        have been separated
    """

    def split_single_node_link(node: TextNode) -> list[TextNode]:
        """A helper function that operates on a single node."""

        new_nodes = []
        link_re = r"\[([^\[\]]*)\]\((.*?)\)"
        tokens = re.split(link_re, node.text)
        for i in range(0, len(tokens) - 1, 3):
            text, alt, url = tokens[i : i + 3]
            new_nodes.append(TextNode(text, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.LINK, url))
        return new_nodes

    return list(map(split_single_node_link, old_nodes))
