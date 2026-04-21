import pytest

from data import (
    BOOK_PRIDE_ZOMBIE,
    BOOK_LOTR,
    BOOK_IT,
    BOOK_INCEPTION,
    BOOK_FIXIKI,
    BOOK_SHREK,
    BOOK_MOYDODYR,
    BOOK_LOVE,
    BOOK_TRACTOR,
    GENRE_COMEDY,
    GENRE_FANTASY,
    GENRE_HORROR,
    GENRE_DETECTIVE,
    GENRE_CARTOONS,
    GENRE_INVALID,
)


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    # 1 проверяем, что добавилось именно две книги в books_genre
    def test_add_new_book_adds_two_books_to_books_genre(self, collector):

        collector.add_new_book(BOOK_PRIDE_ZOMBIE)
        collector.add_new_book(BOOK_LOTR)

        assert len(collector.get_books_genre()) == 2

    # 2 проверяем, что второй раз одна и таже книга не добавилась в books_genre
    def test_add_new_book_does_not_add_duplicate_book(self, collector):

        collector.add_new_book(BOOK_PRIDE_ZOMBIE)
        collector.add_new_book(BOOK_PRIDE_ZOMBIE)

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize("name", ["a", "a" * 39, "a" * 40])
    # 3 проверяем что если у книги валидное количество символов, то книга добавится в books_genre
    def test_add_new_book_adds_book_with_valid_names(self, name, collector):

        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize("name", ["", "a" * 41])
    # 4 проверяем что если у книги невалидное количество символов, то книга не добавится в books_genre
    def test_add_new_book_does_not_adds_book_with_invalid_names(self, name, collector):

        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 0

    # 5 проверяем что существующей книге в books_genre добавляется существующий жанр из genre
    def test_set_book_genre_sets_valid_genre_for_added_book(self, add_books):

        add_books.set_book_genre(BOOK_PRIDE_ZOMBIE, GENRE_COMEDY)

        assert add_books.get_book_genre(BOOK_PRIDE_ZOMBIE) == GENRE_COMEDY

    # 6 проверяем что жанр книги отдается по ее имени верно
    def test_get_book_genre_returns_valid_genre(self, add_books):

        add_books.set_book_genre(BOOK_MOYDODYR, GENRE_CARTOONS)

        assert add_books.get_book_genre(BOOK_MOYDODYR) == GENRE_CARTOONS

    # 7 проверяем что книге правильно присваивается жанр
    def test_get_book_genre_returns_correct_genre(self, add_books):

        add_books.set_book_genre(BOOK_IT, GENRE_HORROR)

        assert add_books.get_book_genre(BOOK_IT) == GENRE_HORROR

    # 8 проверяем что если жанра нет в genre то книге добавляется ""
    def test_set_book_genre_does_not_set_invalid_genre(self, add_books):

        add_books.set_book_genre(BOOK_LOVE, GENRE_INVALID)

        assert add_books.get_book_genre(BOOK_LOVE) == ""

    # 9 проверяем что если книги нет в books_genre то существующий жанр из genre не добавится
    def test_set_book_genre_for_unadded_book_does_not_set_genre(self, collector):

        collector.set_book_genre(BOOK_TRACTOR, GENRE_CARTOONS)

        assert collector.get_book_genre(BOOK_TRACTOR) is None

    # 10 проверяем что выводятся книги с определенным жанром
    def test_get_books_with_specific_genre_returns_correct_books(self, add_books):
        add_books.set_book_genre(BOOK_LOTR, GENRE_FANTASY)

        assert add_books.get_books_with_specific_genre(GENRE_FANTASY) == [BOOK_LOTR]

    # 11 проверяем что если книгу не установлен жанр то будет ''
    def test_get_book_genre_returns_empty_string_for_book_without_genre(
        self, add_books
    ):

        assert add_books.get_book_genre(BOOK_FIXIKI) == ""

    # 12 проверяем что возвращаются книги подходящие детям
    def test_get_books_for_children_returns_books_without_age_rating(self, add_books):

        add_books.set_book_genre(BOOK_PRIDE_ZOMBIE, GENRE_COMEDY)
        add_books.set_book_genre(BOOK_LOTR, GENRE_FANTASY)

        assert add_books.get_books_for_children() == [
            BOOK_PRIDE_ZOMBIE,
            BOOK_LOTR,
        ]

    # 13 проверяем что отсутсвуют книги для детей

    def test_get_books_for_children_returns_empty_list_when_no_suitable_books(
        self, add_books
    ):

        add_books.set_book_genre(BOOK_PRIDE_ZOMBIE, GENRE_HORROR)
        add_books.set_book_genre(BOOK_LOTR, GENRE_DETECTIVE)
        add_books.set_book_genre(BOOK_IT, GENRE_HORROR)
        add_books.set_book_genre(BOOK_INCEPTION, GENRE_DETECTIVE)

        assert add_books.get_books_for_children() == []

    # 14 проверка того что книга добавляется в избранное
    def test_add_book_in_favorites_adds_book_to_favorites(self, add_books):

        add_books.add_book_in_favorites(BOOK_SHREK)

        assert add_books.get_list_of_favorites_books() == [BOOK_SHREK]

    # 15 проверка того что книга удаляется из избранного
    def test_delete_book_from_favorites_removes_book_from_favorites(self, add_books):

        add_books.add_book_in_favorites(BOOK_SHREK)
        add_books.delete_book_from_favorites(BOOK_SHREK)

        assert add_books.get_list_of_favorites_books() == []

    # 16 проверка того что книга  второй раз не добавляется в избранное
    def test_add_book_in_favorites_does_not_add_duplicate_book(self, add_books):

        add_books.add_book_in_favorites(BOOK_SHREK)
        add_books.add_book_in_favorites(BOOK_SHREK)

        assert len(add_books.get_list_of_favorites_books()) == 1

    # 17 проверка метода get_books_genre когда книги добавлены
    def test_get_books_genre_returns_dict_with_added_books(self, add_books):

        assert add_books.get_books_genre() == {
            BOOK_PRIDE_ZOMBIE: "",
            BOOK_LOTR: "",
            BOOK_IT: "",
            BOOK_INCEPTION: "",
            BOOK_FIXIKI: "",
            BOOK_MOYDODYR: "",
            BOOK_LOVE: "",
            BOOK_SHREK: "",
        }

    # 18 проверка метода get_books_genre когда книги не добавлены
    def test_get_books_genre_returns_empty_dict_when_no_books_added(self, collector):

        assert collector.get_books_genre() == {}
