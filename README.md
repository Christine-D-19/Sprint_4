# qa_python

Реализованные тесты:
- test_add_new_book_adds_book #Проверка добавления новой книги
- test_add_new_book_with_long_name_not_added #Нельзя добавить книгу длиннее 40 символов
- test_added_book_has_no_genre #У новой книги жанр пустой
- test_set_book_genre_sets_correct_genre #Установка жанра книги
- test_get_books_with_specific_genre #Получение книг с определённым жанром
- test_get_books_genre_returns_dict #Возвращается словарь books_genre
- test_books_for_children_excludes_age_rated_genres #Книги с возрастным рейтингом не попадают к детям
- test_add_book_in_favorites #Добавление книги в избранное
- test_add_book_in_favorites_only_once #Повторно книга в избранное не добавляется
- test_delete_book_from_favorites #Удаление книги из избранного
