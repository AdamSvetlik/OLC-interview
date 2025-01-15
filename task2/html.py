from enum import Enum
from abc import ABC


Attributes = dict[str, str | None]
Children = list['BaseElement | str'] | None


class ClosureType(Enum):
    UNDEFINED = -1
    CLOSED = 0
    SELF_CLOSING = 1


def format_attributes(attributes: Attributes) -> str:
    attributes_str = ""
    for key, value in attributes.items():
        if value is None:
            attributes_str += f" {key}"
        else:
            attributes_str += f" {key}=\"{value}\""
    return attributes_str


class BaseElement(ABC):
    closure_type: ClosureType = ClosureType.UNDEFINED

    def __init__(self, attributes: Attributes = None):
        if self.closure_type == ClosureType.UNDEFINED:
            raise ValueError("Closure type must be defined")
        if attributes is None:
            attributes = {}
        self.attributes = attributes

    def print(self, indent: int):
        raise NotImplementedError


class ClosedElement(BaseElement, ABC):
    closure_type = ClosureType.CLOSED
    children: Children

    def __init__(self, children: Children, attributes: Attributes = None):
        super().__init__(attributes)
        if children is None:
            children = []
        self.children = children

    def print(self, indent: int = 0):
        tag = self.__class__.__name__.lower()
        print(f"{'  ' * indent}<{tag}", end='')
        print(f"{format_attributes(self.attributes)}>")
        for child in self.children:
            if isinstance(child, str):
                print(f"{'  ' * (indent + 1)}{child}")
            else:
                child.print(indent + 1)
        print(f"{'  ' * indent}</{tag}>")


class SelfClosingElement(BaseElement, ABC):
    closure_type = ClosureType.SELF_CLOSING

    def __init__(self, attributes: Attributes = None):
        super().__init__(attributes)

    def print(self, indent: int = 0):
        print(f"{'  ' * indent}<{self.__class__.__name__.lower()}", end='')
        print(f"{format_attributes(self.attributes)}>")


class Input(SelfClosingElement):
    def __init__(self, attributes: Attributes = None):
        super().__init__(attributes)


class Select(ClosedElement):
    def __init__(self, children: Children = None, attributes: Attributes = None):
        super().__init__(children, attributes)


class A(ClosedElement):
    def __init__(self, children: Children = None, attributes: Attributes = None):
        super().__init__(children, attributes)


class Img(SelfClosingElement):
    def __init__(self, attributes: Attributes = None):
        super().__init__(attributes)


class Div(ClosedElement):
    def __init__(self, children: Children = None, attributes: Attributes = None):
        super().__init__(children, attributes)


class Form(ClosedElement):
    def __init__(self, children: Children = None, attributes: Attributes = None):
        super().__init__(children, attributes)


if __name__ == "__main__":
    Div(
        [
            Form(
                [
                    Input({"type": "text", "name": "name", "placeholder": "Your name"}),
                    Input({"type": "checkbox", "checked": None}),
                    Select(),
                    Input({"type": "submit", "value": "Submit"})
                ]
            ),
            A(["Click me"], {"href": "https://example.com"}),
            Img({"src": "example.png"})
        ], {"class": "container"}).print()


