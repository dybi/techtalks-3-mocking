from unittest import TestCase

from removal_service import remove_file


class TestRemovalFile(TestCase):
    def test_that_non_existing_file_is_not_deleted(self):
        non_existing_file = "sadsadsa.exe"
        remove_file(non_existing_file)
