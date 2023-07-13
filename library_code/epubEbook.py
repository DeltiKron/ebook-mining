
import ebooklib
from ebooklib import epub
from ebook import Ebook
from bs4 import BeautifulSoup


def chapter_to_paragraphs(chapter):
    soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
    text = [para.get_text() for para in soup.find_all('p')]
    return text

class EpubEbook(Ebook):
    file_path = ''
    def get_chapters(self):
        book = epub.read_epub(self.file_path)
        chapters = {}
        for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            print(doc.get_name())
            if 'part' in doc.get_name():
                chapters[doc.get_name()] = chapter_to_paragraphs(doc)
                continue
            # res = nltk.word_tokenize(str(doc.content))
            # text += " ".join([r for r in res if r.isalnum()])
        return chapters.items()
    
    
    @property
    def chapters(self):
        return self.get_chapters()
    
    @classmethod
    def from_file(cls, filename:str):
        assert filename.lower().endswith('.epub'), "This Class needs to be constructed from an '.epub' file"

        instance = cls()
        instance.file_path = filename
        return instance


