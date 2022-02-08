import pyperclip
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from Selenium.Sample_project.GoogleNews.Locators.locators import *
from selenium.webdriver.common.by import By


class CovidPage:

    def __init__(self, driver):
        self.driver = driver

        # Covid-19 ----====----
        self.covid_link = CovidLocator.covid_link_xpath

        # latest
        self.latest_covid = CovidLocator.latest_covid_xpath
        self.latest_news = CovidLocator.latest_news_covid_xpath

        # local
        self.local_covid = CovidLocator.local_covid_xpath
        self.location_local_covid = CovidLocator.location_covid_xpath

        # international
        self.international_covid = CovidLocator.international_covid_xpath
        self.news_covid = CovidLocator.news_title_covid_xpath

    def click_covid(self, covid_19_tag):
        covid = self.driver.find_element(By.XPATH, covid_19_tag)
        covid.click()

        assert True, 'failed'
        print('Clicked successfully')
        sleep(3)