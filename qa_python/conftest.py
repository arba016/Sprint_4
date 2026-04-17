import pytest

from main import BooksCollector
from data import (
    BOOK_PRIDE_ZOMBIE,
    BOOK_LOTR,
    BOOK_IT,
    BOOK_INCEPTION,
    BOOK_FIXIKI,
    BOOK_MOYDODYR,
    BOOK_LOVE,
    BOOK_SHREK,
)


@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture
def add_books(collector):
    collector.add_new_book(BOOK_PRIDE_ZOMBIE)
    collector.add_new_book(BOOK_LOTR)
    collector.add_new_book(BOOK_IT)
    collector.add_new_book(BOOK_INCEPTION)
    collector.add_new_book(BOOK_FIXIKI)
    collector.add_new_book(BOOK_MOYDODYR)
    collector.add_new_book(BOOK_LOVE)
    collector.add_new_book(BOOK_SHREK)
    return collector
