from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    """Returns a new list of TextNode objects where text ndoes are separated
    from formatted nodes."""
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
