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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

@pytest.fixture
def collector():
    return BooksCollector()

# 1. Проверка добавления новой книги
def test_add_new_book_adds_book(collector):
    collector.add_new_book('Гарри Поттер и философский камень')

    assert 'Гарри Поттер и философский камень' in collector.books_genre


# 2. Нельзя добавить книгу длиннее 40 символов
def test_add_new_book_with_long_name_not_added(collector):
    long_name = 'А' * 41
    collector.add_new_book(long_name)
    
    assert long_name not in collector.books_genre


# 3. У новой книги жанр пустой
def test_added_book_has_no_genre(collector):
    collector.add_new_book('Верные враги')
    
    assert collector.get_book_genre('Верные враги') == ''


# 4. Установка жанра книги
def test_set_book_genre_sets_correct_genre(collector):
    collector.add_new_book('Автостопом по галактике')
    collector.set_book_genre('Автостопом по галактике', 'Фантастика')
    
    assert collector.get_book_genre('Автостопом по галатктике') == 'Фантастика'


# 5. Получение книг с определённым жанром
def test_get_books_with_specific_genre(collector):
    collector.add_new_book('Кристина')
    collector.set_book_genre('Кристина', 'Ужасы')
    
    assert collector.get_books_with_specific_genre('Ужасы') == ['Кристина']


# 6. Возвращается словарь books_genre
def test_get_books_genre_returns_dict(collector):
    collector.add_new_book('Старик и море')
    
    assert collector.get_books_genre() == {'Старик и море': ''}


# 7. Книги с возрастным рейтингом не попадают к детям
@pytest.mark.parametrize(
    'book, genre',
    [
        ('Кристина', 'Ужасы'),
        ('Десять негритят', 'Детективы')
    ]
)
def test_books_for_children_excludes_age_rated_genres(collector, book, genre):
    collector.add_new_book(book)
    collector.set_book_genre(book, genre)
    
    assert book not in collector.get_books_for_children()



# 8. Добавление книги в избранное
def test_add_book_in_favorites(collector):
    collector.add_new_book('Убить пересмешника')
    collector.add_book_in_favorites('Убить пересмешника')
    
    assert 'Убить пересмешника' in collector.get_list_of_favorites_books()



 # 9. Повторно книга в избранное не добавляется
def test_add_book_in_favorites_only_once(collector):
    collector.add_new_book('Над пропастью во ржи')
    collector.add_book_in_favorites('Над пропастью во ржи')
    collector.add_book_in_favorites('Над пропастью во ржи')
    
    assert collector.get_list_of_favorites_books().count('Над пропастью во ржи') == 1


# 10. Удаление книги из избранного
def test_delete_book_from_favorites(collector):
    collector.add_new_book('Сто лет одиночества')
    collector.add_book_in_favorites('Сто лет одиночества')
    collector.delete_book_from_favorites('Сто лет одиночества')
    
    assert 'Сто лет одиночества' not in collector.get_list_of_favorites_books()
    