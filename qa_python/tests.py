from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    # 1 проверяем, что добавилось именно пять книг в books_genre
    def test_add_new_book_adds_five_books_to_books_genre(self, add_books):

        assert len(add_books.get_books_genre()) == 5

    # 2 проверяем, что второй раз одна и таже книга не добавилась в books_genre
    def test_add_new_book_does_not_add_duplicate_book(self, add_books):

        add_books.add_new_book("Гордость и предубеждение и зомби")

        # проверяем что словарь имеет длину 2 (две книги)
        assert len(add_books.get_books_genre()) == 5

    # 3 проверяем что если у книги 41 символ, то книга не добавится в books_genre
    def test_add_new_book_does_not_add_book_longer_than_40_chars(self, add_books):

        add_books.add_new_book("Этот короткий текст содержит ровно 41 знак.")

        # проверяем, что добавилось именно две
        assert len(add_books.get_books_genre()) == 5

    # 4 проверяем что существуюущей книге в books_genre добавляется существующий жанр из genre
    def test_set_book_genre_sets_valid_genre_for_added_book(self, add_genre_for_books):

        assert (
            add_genre_for_books.get_book_genre("Гордость и предубеждение и зомби")
            == "Комедии"
        )

    # 5 проверяем что если жанра нет в genre то книге добавляется ''
    def test_set_book_genre_does_not_set_invalid_genre(self):
        collector = BooksCollector()

        collector.add_new_book("Любовь и голуби")
        collector.set_book_genre("Любовь и голуби", "Мелодрама")

        assert collector.get_book_genre("Любовь и голуби") == ""

    # 6 проверяем что если книга нет в books_genre то существующий жанр из genre не добавится
    def test_set_book_genre_for_unadded_book_does_not_set_genre(self):
        collector = BooksCollector()

        collector.set_book_genre("Синий трактор", "Мультфильмы")

        assert "Синий трактор" not in collector.get_books_genre()

    # 7 проверяем что выводятся книги с определенным жанром
    def test_get_books_with_specific_genre_returns_correct_books(
        self, add_genre_for_books
    ):

        assert set(add_genre_for_books.get_books_with_specific_genre("Фантастика")) == {
            "Властелин колец",
        }

    # 8 проверяем что если книгу не установлен жанр то будет ''
    def test_get_book_genre_returns_empty_string_for_book_without_genre(
        self, add_books
    ):
        assert add_books.get_book_genre("Фиксики") == ""

    # 9 проверяем что книге правильно присваивается жанр
    def test_get_book_genre_returns_correct_genre(self, add_genre_for_books):

        assert add_genre_for_books.get_book_genre("Оно") == "Ужасы"

    # 10 проверяем что возвращаются книги подходящие детям
    def test_get_books_for_children_returns_books_without_age_rating(
        self, add_genre_for_books
    ):

        assert add_genre_for_books.get_books_for_children() == [
            "Гордость и предубеждение и зомби",
            "Властелин колец",
        ]

    # 11 проверяем что отсутсвуют книги для детей

    def test_get_books_for_children_returns_empty_list_when_no_suitable_books(
        self, add_books
    ):

        add_books.set_book_genre("Гордость и предубеждение и зомби", "Ужасы")
        add_books.set_book_genre("Властелин колец", "Детективы")
        add_books.set_book_genre("Оно", "Ужасы")
        add_books.set_book_genre("Начало", "Детективы")

        assert add_books.get_books_for_children() == []

    # 12 проверка того что книга добавляется в избранное
    def test_add_book_in_favorites_adds_book_to_favorites(self, add_favorit_book):

        assert add_favorit_book.get_list_of_favorites_books() == ["Шрек"]

    # 13 проверка того что книга удаляется из избранного
    def test_delete_book_from_favorites_removes_book_from_favorites(
        self, add_favorit_book
    ):

        add_favorit_book.delete_book_from_favorites("Шрек")

        assert add_favorit_book.get_list_of_favorites_books() == []

    # 14 проверка того что книга  второй раз не добавляется в избранное
    def test_add_book_in_favorites_does_not_add_duplicate_book(self, add_favorit_book):

        add_favorit_book.add_book_in_favorites("Шрек")

        assert len(add_favorit_book.get_list_of_favorites_books()) == 1
