import unittest

class BuildUrlTest(unittest.TestCase):
    def test_build_url(self):
        from booksearch.api import build_url
        expected = 'https://www.googleapis.com/books/v1/volumes?q=python'
        actual = build_url({'q': 'python'})
        self.assertEqual(expected, actual)

        # 만약 위의 test가 실패하면 이 아래쪽부터는 실행되지 않음.
        # 때문에 아예 분리를 하면 한번의 테스트로 많은 것을 확인이 가능

    def test_build_url_empty_param(self):
        from booksearch.api import build_url
        expected = 'https://www.googleapis.com/books/v1/volumes?'
        actual = build_url({})
        self.assertEqual(expected, actual)

    # 실패하는 test는 이 decorator를 추가하면 pass 가능.
    @unittest.expectedFailure
    def test_build_url_fail(self):
        from booksearch.api import build_url
        expected = 'https://www.googleapis.com/books/v1/volumes'
        actual = build_url({})
        self.assertEqual(expected, actual, msg='this test will be fail.') 
