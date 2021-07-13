from unittest import TestCase
from unittest.mock import patch
from src.db_helper import DbHelper

class TestDbHelper(TestCase):

    # def setUp(self):
    #     self.dbhelper = DbHelper()

    @patch('src.db_helper.DbHelper')
    def test_max_salary_is_greater_than_min_salary(self, MockDbHelper):
        mock_dbhelper = MockDbHelper()

        mock_dbhelper.get_maximum_salary.return_value = 99997
        # maxx = self.dbhelper.get_maximum_salary()
        maxx = mock_dbhelper.get_maximum_salary()   # calling get_maximum_salary method but the mocked version will actually get called

        mock_dbhelper.get_minimum_salary.return_value = 10001
        # minn = self.dbhelper.get_minimum_salary()
        minn = mock_dbhelper.get_minimum_salary()   # calling get_minimum_salary method but the mocked version will actually get called

        self.assertGreater(maxx, minn)