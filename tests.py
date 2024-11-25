import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    # проверка добавления одной книги
    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гранатовый браслет')
        assert 'Гранатовый браслет' in collector.get_books_genre()

    # проверка добавления двух книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Бедная Лиза')
        assert len(collector.get_books_genre()) == 2

    #проверка добавления книги с невалидной длиной названия больше 40 символов
    def test_add_new_book_with_long_name(self):
        collector = BooksCollector()
        long_book_name = 'Облачно, возможны осадки в виде фрикаделек'
        collector.add_new_book(long_book_name)
        assert long_book_name not in collector.get_books_genre()

    #проверка, что нельзя добавить одну и ту же книгу повторно
    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        book_name = '1408'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        books_genre = collector.get_books_genre()
        assert list(books_genre.keys()).count(book_name) == 1 #проверка что книга добавлена только 1 раз

    # проверка установки жанра книги (метод set_book_genre), после установки жанра, он корректно сохраняется
    @pytest.mark.parametrize("book_name,genre", [
        ('Книга 1', 'Фантастика'),
        ('Книга 2', 'Мультфильмы'),
    ])
    def test_set_book_genre_parametrized(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    #Проверка что нельзя установить жанр не из списка genre для новой книги (невалидный жанр)
    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        book_name = 'Под куполом'
        collector.add_new_book(book_name)
        invalid_genre = 'Фанфик'
        collector.set_book_genre(book_name, invalid_genre)
        assert collector.get_book_genre(book_name) == '' #проверка что что жанр остался пустой

    #Проверка установки жанра из списка для не добавленной книги
    def test_set_book_genre_book_not_in_genre(self):
        collector = BooksCollector()
        book_name = 'Покемоны'
        genre = 'Фантастика'
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) is None # проверка что жанр не был установлен, так как книга не добавлена в books_genre

    #Проверка получения жанра для добавленной книги (get_book_genre возвращает жанр, который был установлен для книги)
    def test_get_book_genre(self):
        collector = BooksCollector()
        book_name = 'Хоббит'
        genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    #Получить список книг с определенным жанром
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Ужасы')
        books = collector.get_books_with_specific_genre('Фантастика')
        assert 'Книга 1' in books and 'Книга 2' not in books

    #Проверяем , что метод get_books_genre возвращает нужный словарь
    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Фантастика')
        expected_books_genre = {'Книга 1': 'Фантастика','Книга 2': '' }
        assert collector.get_books_genre() == expected_books_genre

    #Проверка получения списка книг для детей
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Мультфильмы')
        collector.set_book_genre('Книга 2', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert 'Книга 1' in children_books and 'Книга 2' not in children_books

    #проверка добавление в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        assert 'Книга 1' in collector.get_list_of_favorites_books()

    #Проверка что нельзя добавить в избранное одну и туже книгу
    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        assert len(collector.get_list_of_favorites_books()) == 1

    # Проверка получения списка двух избранных книг
    def test_get_list_of_favorites_books_only_two(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 2')

        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 2

    #Проверка удаления книги из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга Илая')
        collector.add_book_in_favorites('Книга Илая')
        collector.delete_book_from_favorites('Книга Илая')
        assert 'Книга Илая' not in collector.get_list_of_favorites_books()
