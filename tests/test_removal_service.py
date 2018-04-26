from unittest import TestCase
from unittest.mock import patch

from removal_service import remove_file


class TestRemovalFile(TestCase):
    def test_that_non_existing_file_is_not_deleted(self):
        non_existing_file = "sadsadsa.exe"
        remove_file(non_existing_file)

    @patch("os.path.exists", return_value=True)
    @patch("os.path.isdir", return_value=True)
    def test_that_existing_directory_is_not_deleted(self, isdir_mock, exists_mock):
        existing_dir = "/tmp"

        remove_file(existing_dir)

        exists_mock.assert_called_once_with(existing_dir)
        isdir_mock.assert_called_once_with(existing_dir)
