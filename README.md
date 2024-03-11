# qa_python
- `test_add_new_book_add_two_books` — проверка добавления методом add_new_book двух книг в словарь;

- `test_add_new_book_added_book_has_empty_genre_true` — проверка, что книга добавляется с пустым значением жанра;

- `test_add_new_book_invalid_length_name_not_added` — проверка невалидных значений длины названия при добавлении книги в словарь;

- `test_set_book_genre_true` — проверка метода set_book_genre, который присваивает жанр книге;
 
- `test_get_book_genre_true` — проверка метода get_book_genre, который получает жанр книги;
 
- `test_get_books_with_specific_genre_valid_genre_true` — проверка метода get_books_with_specific_genre, который возвращает список книг указанного жанра;
 
- `test_get_books_for_children_book_without_age_rating_true` — проверка метода get_books_for_children со словарем из одной книги без возрастных ограничений;
 
- `test_get_books_for_children_books_with_age_rating_not_added`  — проверка работы метода get_books_for_children со словарем книг для разных возрастов; 
 
- `test_add_book_in_favorites_recurring_book_is_added_once` — проверка работы метода add_book_in_favorites при попытке добавить в favorites уже существующую там книгу;
 
- `test_delete_book_from_favorites_valid_name_true` — проверка работы метода delete_book_from_favorites, удаляющего книгу из favorites;
 
- `test_get_list_of_favorites_books_true` — проверка работы метода get_list_of_favorites, получающего список favorites;

- Метод `get_books_genre` покрывается первым тестом.