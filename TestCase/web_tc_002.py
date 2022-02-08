import time

from Selenium.Sample_project.GoogleNews.Pages.base_page import BasePage
from Selenium.Sample_project.GoogleNews.Pages.search_page import SearchPage
from Selenium.Sample_project.GoogleNews.Tests.base_test import BaseTest


class TestCase2(BaseTest):

    # Featured topic news
    def test_tc_1(self):
        base_call = BasePage(self.driver)
        base_call.search()

        # click featured topic on search bar
        SearchPage(self.driver).click_featured_topic()
        time.sleep(5)

    # Latest news
    def test_tc_2(self):
        base_call = BasePage(self.driver)
        base_call.search()

        # click news on search bar
        SearchPage(self.driver).click_news()
        time.sleep(5)





# def call_url(self):
    #     driver = self.driver
    #     driver.get('https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en')
    #     time.sleep(10)
    #
    # def search(self):
    #     # click on search
    #     search = SearchPage(self.driver)
    #     search.click_search_bar()
    #     time.sleep(2)