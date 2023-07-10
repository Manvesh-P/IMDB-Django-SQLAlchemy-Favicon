import requests
from unittest import TestCase
import unittest
from logger_files.test_custom_logger import logger


class TestActualLogicServer(TestCase):
    def test_get_director_with_max_number_of_movies(self):
        logger.info('test-1 started')

        res = requests.get('http://127.0.0.1:8000/get/director/with/max/number/of/movies/')
        res_1 = res.text

        self.assertTrue(bool(~res_1.find('Stanley Kubrick')) == True)
        self.assertFalse(bool(~res_1.find('Giovanni Pastrone')) == True)
        self.assertEqual(bool(~res_1.find('Stanley Kubrick')), True)

        logger.info('test-1 ended')

    def test_get_top_ten_movies_based_on_imdb_score(self):
        logger.info('test-2 started')

        res = requests.get('http://127.0.0.1:8000/get/top/ten/movies/based/on/imdb_score/')
        res_1 = res.text

        self.assertTrue(bool(~res_1.find("'The Twilight Zone', 9.5")) == True)
        self.assertTrue(bool(~res_1.find("'The Godfather', 9.2")) == True)
        self.assertTrue(bool(~res_1.find("'The Simpsons', 9.0")) == True)
        self.assertTrue(bool(~res_1.find("'Star Wars', 8.8")) == True)
        self.assertFalse(bool(~res_1.find("'Casablanca', 8.8")) == False)
        self.assertFalse(bool(~res_1.find("'The X Files', 9.0")) == False)
        self.assertEqual(bool(~res_1.find("'I Love Lucy', 9.0")), True)

        logger.info('test-2 ended')

    def test_get_least_watched_movie_based_on_imdb_score(self):
        logger.info('test-3 started')

        res = requests.get('http://127.0.0.1:8000/get/least/watched/movie/based/on/imdb_score/')
        res_1 = res.text

        self.assertTrue(bool(~res_1.find('The Tin Man')) == True)
        self.assertFalse(bool(~res_1.find('The Twilight Zone')) == True)
        self.assertEqual(bool(~res_1.find('The Tin Man')), True)

        logger.info('test-3 ended')

    def test_get_most_watched_genre(self):

        logger.info('test-4 started')

        res = requests.get('http://127.0.0.1:8000/get/most/watched/genre/')
        res_1 = res.text

        self.assertTrue(bool(~res_1.find('Drama')) == True)
        self.assertFalse(bool(~res_1.find('News')) == True)
        self.assertEqual(bool(~res_1.find('Drama')), True)

        logger.info('test-4 ended')

    def test_get_most_popular_director_in_first_hundread_movies(self):
        logger.info('test-5 started')

        res = requests.get('http://127.0.0.1:8000/get/most/popular/director/in/first/hundread/movies/')
        res_1 = res.text

        self.assertTrue(bool(~res_1.find('John Brahm')) == True)
        self.assertFalse(bool(~res_1.find('James Parrott')) == True)
        self.assertEqual(bool(~res_1.find('John Brahm')), True)

        logger.info('test-5 ended')



if __name__ == '__main__':
    unittest.main()


