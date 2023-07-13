from unittest import TestCase
from library_code.lib.ebubEbook import EpubEbook
import unittest


class TestEpubEbook(TestCase):
    def test_basics(self):
        book = EpubEbook.from_file('../data/Discworld 04 - Mort - Pratchett_ Terry.epub')
        for c in book.chapters:
            for i,p in enumerate(c):
                print(i,len(p), p[:10])
if __name__ == '__main__':
    unittest.main()