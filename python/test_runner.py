# python/test_runner.py
import unittest
from logger import setup_logger

logger = setup_logger('test_runner', 'test_runner.log')

class TestApp(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2, "1+1 should equal 2")
        logger.info("Test 'test_example' passed.")

if __name__ == '__main__':
    try:
        unittest.main()
        logger.info("Tests executed successfully.")
    except Exception as e:
        logger.error(f"Test execution failed: {e}")
