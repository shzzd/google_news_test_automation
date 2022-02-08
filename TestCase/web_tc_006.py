from time import sleep

from Selenium.Sample_project.GoogleNews.Pages.base_page import BasePage
from Selenium.Sample_project.GoogleNews.Tests.base_test import BaseTest


class TestCase6(BaseTest):
    # =============================================== Saved searches ===================================================
    # saved searches
    def test_tc_1(self):
        BasePage(self.driver, url='https://news.google.com/my/searches?hl=en-US&gl=US&ceid=US%3Aen')
        sleep(7)
