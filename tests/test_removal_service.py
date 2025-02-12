from unittest import TestCase
from unittest.mock import patch

from removal_service import remove_file


class TestRemovalFile(TestCase):
    def setUp(self):
        patcher = patch("os.remove")
        self.remove_mock = patcher.start()
        self.addCleanup(patcher.stop)

    @patch("os.path.exists", return_value=True)
    def test_that_non_existing_file_is_not_deleted(self, exists_mock):
        non_existing_file = "sadsadsa.exe"

        remove_file(non_existing_file)

        exists_mock.assert_called_once_with(non_existing_file)
        self.remove_mock.assert_not_called()

    @patch("os.path.exists", return_value=True)
    @patch("os.path.isdir", return_value=True)
    def test_that_existing_directory_is_not_deleted(self, isdir_mock, exists_mock):
        existing_dir = "/tmp"

        remove_file(existing_dir)

        exists_mock.assert_called_once_with(existing_dir)
        isdir_mock.assert_called_once_with(existing_dir)
        self.remove_mock.assert_not_called()

    @patch("os.path.exists", return_value=True)
    @patch("os.path.isfile", return_value=True)
    def test_that_existing_file_is_deleted(self, isfile_mock, exists_mock):
        existing_file = "i_exist_therefore_delete.me"

        remove_file(existing_file)

        exists_mock.assert_called_once_with(existing_file)
        isfile_mock.assert_called_once_with(existing_file)
        self.remove_mock.assert_called_once_with(existing_file)
