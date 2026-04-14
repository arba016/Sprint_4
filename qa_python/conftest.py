import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture
def add_books(collector):

    collector.add_new_book("Гордость и предубеждение и зомби")
    collector.add_new_book("Властелин колец")
    collector.add_new_book("Оно")
    collector.add_new_book("Начало")
    collector.add_new_book("Фиксики")
    return collector


@pytest.fixture
def add_genre_for_books(add_books):

    add_books.set_book_genre("Гордость и предубеждение и зомби", "Комедии")
    add_books.set_book_genre("Властелин колец", "Фантастика")
    add_books.set_book_genre("Оно", "Ужасы")
    add_books.set_book_genre("Начало", "Детективы")
    return add_books


@pytest.fixture
def add_favorit_book(collector):
    collector.add_new_book("Шрек")
    collector.add_book_in_favorites("Шрек")

    return collector
