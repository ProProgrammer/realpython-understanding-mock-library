import unittest
from unittest.mock import patch

from requests.exceptions import Timeout

from my_calendar_patch_decorator import get_holidays


class TestCalendar(unittest.TestCase):
    @patch('my_calendar_patch_decorator.requests')
    def test_get_holidays_timeout(self, mock_requests):
        mock_requests.get.side_effect = Timeout

        with self.assertRaises(Timeout):
            get_holidays()

        mock_requests.get.assert_called_once_with('http://localhost/api/holidays')


if __name__ == '__main__':
    unittest.main()
