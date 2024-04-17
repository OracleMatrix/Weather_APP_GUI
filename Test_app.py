import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from Main import get_info


class TestWeatherApp(unittest.TestCase):

    @patch('requests.get')
    def test_get_info(self, mock_requests):
        mock_data = {
            'weather': [{'main': 'Clouds'}],
            'main': {'temp': 280, 'pressure': 1018, 'humidity': 75}
        }
        mock_requests.return_value.json.return_value = mock_data

        get_info()

        # Add your assertions here based on the changes made by get_info function


if __name__ == "__main__":
    unittest.main()