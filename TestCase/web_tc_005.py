from time import sleep

from Selenium.Sample_project.GoogleNews.Pages.base_page import BasePage
from Selenium.Sample_project.GoogleNews.Tests.base_test import BaseTest


class TestCase5(BaseTest):
    # ============================================== Topic & Sources ===================================================
    # go to Topic & sources on Following
    def test_tc_1(self):
        BasePage(self.driver, url='https://news.google.com/my/library?hl=en-US&gl=US&ceid=US%3Aen')
        sleep(3)

    # =============================================== Saved searches ===================================================
    # saved searches
    def test_tc_2(self):
        BasePage(self.driver, url='https://news.google.com/my/searches?hl=en-US&gl=US&ceid=US%3Aen')
        sleep(3)

    # =============================================== Saved stories ====================================================
    # saved stories
    def test_tc_3(self):
        BasePage(self.driver, url='https://news.google.com/my/bookmarks?hl=en-US&gl=US&ceid=US%3Aen')
        sleep(3)
