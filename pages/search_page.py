from Selenium.Sample_project.GoogleNews.Locators.locators import *
from selenium.webdriver.common.by import By


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

        self.search_box_css = SearchPageLocator.search_box_css
        self.google_text_css = SearchPageLocator.google_text_css

        self.featured_topic_box_css = SearchPageLocator.featured_topic_box_css
        self.featured_topic_name_css = SearchPageLocator.featured_topic_name_css

        self.news_box_css = SearchPageLocator.news_box_css
        self.news_name_css = SearchPageLocator.news_name_css

    def click_search_bar(self):
        # google_text = self.driver.find_element(By.XPATH, self.google_text_css)
        search_bar = self.driver.find_element(By.XPATH, self.search_box_css)
        search_bar.click()

        assert True, 'failed'
        print('clicked on search bar')

    def click_featured_topic(self):
        featured_topic_box = self.driver.find_element(By.XPATH, self.featured_topic_box_css)
        # feature_name = self.driver.find_element(By.XPATH, self.featured_topic_name_css)
        featured_topic_box.click()

        assert True, 'failed'
        print('clicked on featured topic')

    def click_news(self):
        news_box = self.driver.find_element(By.XPATH, self.news_box_css)
        # news_name = self.driver.find_element(By.CSS_SELECTOR, self.news_name_css)
        news_box.click()

        assert True, 'failed'
        print('clicked on news')