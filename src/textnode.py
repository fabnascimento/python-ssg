from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = "normal"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK_TEXT = "link"
    IMAGE_TEXT = "image"

class TextNode:

    def __init__(self, text: str, text_type: TextType, url: str) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, TextNode):
            return False
        
        # I need to test to see if that is faster than iterating
        # over the object
        return self.text == value.text and self.text_type == value.text_type and self.url == value.url
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"