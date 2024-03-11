from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test


class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_added_book_has_empty_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Тошнота')
        assert collector.books_genre['Тошнота'] == ''

    @pytest.mark.parametrize('name', [
        '',
        '12345678901234567890123456789012345678901',
        '123456789012345678901234567890123456789012345678901234567890'])
    def test_add_new_book_invalid_length_name_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.books_genre == {}

    def test_set_book_genre_true(self):
        collector = BooksCollector()
        collector.books_genre = \
            {
                'Сказка о царе Салтане, о сыне его славном и могучем богатыре князе Гвидоне Салтановиче '
                'и о прекрасной царевне Лебеди':
                    'Мультфильмы',
                'Клуб самоубийц':
                    'Детективы',
                'Падение дома Ашеров':
                    'Ужасы',
                'Кровь эльфов':
                    ''
            }
        collector.set_book_genre('Кровь эльфов', 'Фантастика')
        assert collector.books_genre['Кровь эльфов'] == 'Фантастика'

    @pytest.mark.parametrize('name', [
        'Сказка о царе Салтане, о сыне его славном и могучем богатыре князе Гвидоне Салтановиче '
        'и о прекрасной царевне Лебеди',
        'Клуб самоубийц',
        'Падение дома Ашеров',
        'Кровь эльфов',
        ])
    def test_get_book_genre_true(self, name):
        collector = BooksCollector()
        collector.books_genre = \
            {
                'Сказка о царе Салтане, о сыне его славном и могучем богатыре князе Гвидоне Салтановиче '
                'и о прекрасной царевне Лебеди':
                    'Мультфильмы',
                'Клуб самоубийц':
                    'Детективы',
                'Падение дома Ашеров':
                    'Ужасы',
                'Кровь эльфов':
                    'Фантастика'
            }
        assert collector.get_book_genre(name) == collector.books_genre[name]

    def test_get_books_with_specific_genre_valid_genre_true(self):
        collector = BooksCollector()
        collector.books_genre = \
            {
                'Сказка о царе Салтане, о сыне его славном и могучем богатыре князе Гвидоне Салтановиче '
                'и о прекрасной царевне Лебеди':
                    'Мультфильмы',
                'Клуб самоубийц':
                    'Детективы',
                'Падение дома Ашеров':
                    'Ужасы',
                'Кровь эльфов':
                    'Фантастика'
            }
        assert collector.get_books_with_specific_genre('Детективы') == ['Клуб самоубийц']

    def test_get_books_for_children_book_without_age_rating_true(self):
        collector = BooksCollector()
        collector.books_genre = {
            'Сказка о царе Салтане, о сыне его славном и могучем богатыре князе Гвидоне Салтановиче '
            'и о прекрасной царевне Лебеди':
                'Мультфильмы'}
        assert collector.get_books_for_children() == [
            'Сказка о царе Салтане, о сыне его славном и могучем богатыре князе Гвидоне Салтановиче '
            'и о прекрасной царевне Лебеди']

    def test_get_books_for_children_books_with_age_rating_not_added(self):
        collector = BooksCollector()
        collector.books_genre = {
            'Сказка о царе Салтане, о сыне его славном и могучем богатыре князе Гвидоне Салтановиче '
            'и о прекрасной царевне Лебеди':
                'Мультфильмы',
            'Клуб самоубийц':
                'Детективы',
            'Падение дома Ашеров':
                'Ужасы'}
        assert collector.get_books_for_children() == [
            'Сказка о царе Салтане, о сыне его славном и могучем богатыре князе Гвидоне Салтановиче '
            'и о прекрасной царевне Лебеди']

    def test_add_book_in_favorites_recurring_book_is_added_once(self):
        collector = BooksCollector()
        collector.books_genre = {'Клуб самоубийц': ''}
        collector.favorites = ['Клуб самоубийц']
        collector.add_book_in_favorites('Клуб самоубийц')
        assert collector.favorites == ['Клуб самоубийц'] and len(collector.favorites) == 1

    def test_delete_book_from_favorites_valid_name_true(self):
        collector = BooksCollector()
        collector.favorites = ['Клуб самоубийц', 'Кровь эльфов', 'Тошнота', 'Процесс']
        collector.delete_book_from_favorites('Процесс')
        assert collector.favorites == ['Клуб самоубийц', 'Кровь эльфов', 'Тошнота']

    def test_get_list_of_favorites_books_true(self):
        collector = BooksCollector()
        collector.favorites = ['Клуб самоубийц', 'Кровь эльфов', 'Тошнота', 'Процесс']
        assert collector.get_list_of_favorites_books() == collector.favorites




