from __future__ import annotations
from abc import ABC, abstractmethod


class Dialog(ABC):
    '''
    The Creator
    '''
    def __init__(self, w, h) -> None:
        self.w = w
        self.h = h

    @abstractmethod
    def createButton(self):
        pass

    def render(self):
        okButton = self.createButton()
        print(okButton.render(self.w, self.h))   
        f = "closeDialog"
        print(okButton.onClick(f))

class WindowsDialog(Dialog):
    def __init__(self, w, h) -> None:
        super().__init__(w, h)

    def createButton(self):
        return WindowsButton()

class WebDialog(Dialog):
    def __init__(self, w, h) -> None:
        super().__init__(w, h)

    def createButton(self):
        return HTMLButton()

class Button(ABC):
    """
    The Button interface declares the operations that all concrete products
    must implement.
    """
    @abstractmethod
    def render():
        pass
    @abstractmethod
    def onClick(f):
        pass

class WindowsButton(Button):
    """
    Concrete Product
    """
    def render(self, w, h):
        return 'The Windows Button created with width {} and height {}'.format(w, h)
    def onClick(self, f):
        return 'Windows -Event on click {}'.format(f)

class HTMLButton(Button):
    """
    Concrete Product
    """
    def render(self, w, h):
        return 'The HTML Button created with width {} and height {}'.format(w, h)
    
    def onClick(f):
        return 'WEB -Event on click {}'.format(f)

class Application:
    def __init__(self, OS, w, h) -> None:
        self.OS = OS
        self.w = w
        self.h = h
    
    def initialize(self):
        if self.OS == "Windows":
            return WindowsDialog(self.w, self.h)
        elif self.OS == "Web":
            return WebDialog(self.w, self.h)
        else:
            raise Exception("Error! Unknown operating system.")

if __name__ == "__main__":
    app = Application("Windows", 20, 10)
    dialog = app.initialize()
    dialog.createButton()
    dialog.render()
