from abc import ABC, abstractclassmethod, abstractmethod


class Ebook(ABC):
    @abstractmethod
    def get_chapters(self):
        pass
    
    @abstractclassmethod
    def from_file():
        pass

class Chapter():
    paragraphs: list[str]
    def __init__(self, paragraphs:list[str], title=None):
        self.paragraphs = paragraphs
    def __iter__(self):
        return (p for p in self.paragraphs)


