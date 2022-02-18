import pathlib
import unittest
from tempfile import TemporaryDirectory
from unittest.mock import patch 

THUMBNAIL_URL = (
    'http://books.google.com/books/content'
    '?id=OgtBw760Y5EC&printsec=frontcover'
    '&img=1&zoom=1&edge=curl&source=gbs_api'
)

class SaveThumbnailsTest(unittest.TestCase):
    def setUp(self):
        # 임시 디렉터리 작성
        self.tmp = TemporaryDirectory()

    def tearDown(self):
        # 임시 디렉터리 정리
        self.tmp.cleanup()

    def test_save_thumbnails(self):
        from booksearch.core import Book
        book = Book({'id':'', 'volumeInfo':{
            'imageLinks':{
                'thumbnail' : THUMBNAIL_URL
            }}})

        filename = book.save_thumbnails(self.tmp.name)[0]
        self.assertTrue(pathlib.Path(filename).exists())

    @patch ('booksearch.core.get_data')
    def test_save_thumbnails(self, mock_get_data):
        from booksearch.core import Book
        data_path = pathlib.Path(__file__).with_name('data')
        mock_get_data.return_value = (
            data_path / 'puFBDwAAQBAJ_thumbnail.jpeg').read_bytes()

        book = Book({'id': '', 'volumeInfo' : {
            'imageLinks': {
                'thumbnail': THUMBNAIL_URL
            }}})
        
        filename = book.save_thumbnails(self.tmp.name)[0]
        mock_get_data.assert_called_with(THUMBNAIL_URL)

        self.assertEqual( mock_get_data.return_value, filename.read_bytes())


if __name__ == '__main__' :
    unittest.main()