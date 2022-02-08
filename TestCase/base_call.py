import time
from Selenium.Sample_project.GoogleNews.Pages.search_page import SearchPage


class BaseCall:
    def __init__(self, driver, url='https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en'):
        self.driver = driver
        self.driver.get(url)
        time.sleep(2)

    def search(self):
        # click on search
        search = SearchPage(self.driver)
        search.click_search_bar()
        time.sleep(2)