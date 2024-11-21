from __future__ import annotations
from typing import Optional, Iterable


class HTMLNode:
    """Base class for reprenting HTML elements

    Attributes
    ----------
    tag : str, optional
        An HTML tag that is prefixed and suffixed to the text content
    value : str, optional
        Text content of an HTML node
    children : Iterable[HTMLNode], optional
        All HTML nodes contained within the current node
    props : dict[str,str], optional
        Attributes of an HTML node used for passing additional metadata
    """

    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[Iterable[HTMLNode]] = None,
        props: Optional[dict[str, str]] = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented

    def props_to_html(self) -> str:
        """Converts are dictionary into key-value attributes.

        Returns
        -------
        str
            an HTML string with attributes included in tags
        """

        if self.props:
            s = "".join([f'{attr}="{val}"' for attr, val in self.props.items()])
            return " " + s
        return ""

    def __repr__(self) -> str:
        """Pretty prints the attributes of the HTMLNode class."""
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    """An HTMLNode that has no children

    Attributes
    ----------
    tag : str, optional
        An HTML tag that is prefixed and suffixed to the text content
    value : str, optional
        Text content of an HTML node
    props : dict[str,str], optional
        Attributes of an HTML node used for passing additional metadata
    """

    def __init__(
        self, tag: Optional[str], value: str, props: Optional[dict[str, str]] = None
    ) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("missing value")
        if self.tag is None:
            # return raw text
            return self.value
        # return a rendered HTML tag
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    """An HTMLNode that has at least one child node

    Attributes
    ----------
    tag : str, optional
        An HTML tag that is prefixed and suffixed to the text content
    value : str, optional
        Text content of an HTML node
    children : Iterable[HTMLNode]
        All HTML nodes contained within the current node
    props : dict[str,str], optional
        Attributes of an HTML node used for passing additional metadata
    """

    def __init__(
        self,
        tag: str,
        children: Iterable[HTMLNode],
        props: Optional[dict[str, str]] = None,
    ):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        """Recursively renders the HTML string of children nodes and concatenates
        them into a single string

        Returns
        -------
        str
            An HTML string containing metadata from the ParentNode and all children nodes
        """
        if self.tag is None:
            raise ValueError("missing tag")
        if len(self.children) == 0:
            raise ValueError("must have at least one child node")

        html = f"<{self.tag}{self.props_to_html()}>"
        # recursively add children node
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html
