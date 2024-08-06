
import unittest
from app import create_app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_convert_image(self):
      
        pass

    def test_convert_pdf(self):
      
        pass

if __name__ == '__main__':
    unittest.main()
