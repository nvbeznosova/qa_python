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
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_does_not_add_duplicates(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 1")
        assert len(collector.get_books_genre()) == 1
    
    def test_add_new_book_invalid_names_not_added(self):
        collector = BooksCollector()
        collector.add_new_book ("")
        collector.add_new_book("A" * 62)
        assert len(collector.get_books_genre()) == 0

    def test_added_book_has_no_genre_initially(self):
        collector = BooksCollector()
        collector.add_new_book("Воспитание чувств")
        assert collector.get_book_genre("Воспитание чувств") == ""
    
    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.set_book_genre("Книга 1", "Фантастика")
        result = collector.get_book_genre ("Книга 1")
        assert result == "Фантастика"
    
    def test_set_book_genre_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Двадцать тысяч лье под водой")
        collector.set_book_genre("Двадцать тысяч лье под водой", "Фантастика")
        assert collector.get_book_genre("Двадцать тысяч лье под водой") == "Фантастика"
    
    def test_set_book_genre_invalid_genre_does_not_change(self):
        collector = BooksCollector()
        collector.add_new_book ("Двадцать тысяч лье под водой")
        collector.set_book_genre("Двадцать тысяч лье под водой", "Несуществущий жанр")
        assert collector.get_book_genre("Двадцать тысяч лье под водой") == ""
    
    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.set_book_genre("Книга 1", "Фантастика")
        collector.add_new_book("Книга 2")
        collector.set_book_genre("Книга 2", "Ужасы")
        result = collector.get_books_with_specific_genre("Фантастика")
        assert result == ["Книга 1"]

    def test_get_books_genre_returns_all_books(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        genres = collector.get_books_genre()
        assert "Книга 1" in genres
        assert "Книга 2" in genres
        assert isinstance(genres,dict)

    @pytest.mark.parametrize("genre", ["Ужасы", "Детективы"])
    def test_get_books_for_children_excludes_age_restricted(self, genre):
        collector = BooksCollector()
        collector.add_new_book("Страшная книга")
        collector.set_book_genre("Страшная книга", genre)
        assert "Страшная книга" not in collector.get_books_for_children()
    
    @pytest.mark.parametrize("genre", ["Фантастика", "Мультфильмы", "Комедии"])
    def test_get_books_for_children_includes_only_safe_genres(self, genre):
        collector = BooksCollector()
        collector.add_new_book("Детская книга")
        collector.set_book_genre("Детская книга", genre)
        assert "Детская книга" in collector.get_books_for_children()
    
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.add_book_in_favorites("Книга 1")
        assert collector.get_list_of_favorites_books() == ["Книга 1"]

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.add_book_in_favorites("Книга 1")
        collector.delete_book_from_favorites ("Книга 1")
        assert collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_does_not_add_twice(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.add_book_in_favorites("Книга 1")
        collector.add_book_in_favorites("Книга 1")
        assert collector.get_list_of_favorites_books().count("Книга 1") == 1

