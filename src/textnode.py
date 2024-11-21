from __future__ import annotations
from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    """Container for a Markdown-formatted string

    Attributes
    ----------
    text : str
        The raw string cotent
    text_type : TextType
        Symbolic representation of a portion of the content often used to style its appearance
    url : str, optional
        Hyperlinks used in including links and images in Markdown
    """

    def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: TextNode) -> bool:
        """Equality of all attributes are compared"""
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self) -> str:
        """Pretty print the attributes of a TextNode"""
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
