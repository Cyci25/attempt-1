import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    def setUp(self):
        self.new_news = News(1234,'Why me ??', 'Why not you?', 'https://image.tmdb.org/t/p/w500/khsjha27hbs','8.5','123654')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()
