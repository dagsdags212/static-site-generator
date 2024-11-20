from __future__ import annotations
from typing import Optional, Iterable


class HTMLNode:
    """Base class for reprenting HTML elements."""

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
        """Returns a string that represents HTML attributes of a node."""
        if self.props:
            s = "".join([f'{attr}="{val}"' for attr, val in self.props.items()])
            return " " + s
        return ""

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    """HTMLNode with no children."""

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
    def __init__(
        self,
        tag: str,
        children: Iterable[HTMLNode],
        props: Optional[dict[str, str]] = None,
    ):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
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
