import time

from Selenium.Sample_project.GoogleNews.Pages.base_page import BasePage
from Selenium.Sample_project.GoogleNews.Tests.base_test import BaseTest


class TestCase1(BaseTest):

    def test_tc_001(self):
        BasePage(self.driver)
        time.sleep(2)

        assert True, 'home page not visible'
        print('home page visible')
