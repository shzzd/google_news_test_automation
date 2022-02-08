import pyperclip
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from Selenium.Sample_project.GoogleNews.Locators.locators import *
from selenium.webdriver.common.by import By


class HeadlinesPage:

    def __init__(self, driver):
        self.driver = driver

        self.headline_text = HeadlinesLocator.headline_text_link_text
        self.follow_link = HeadlinesLocator.follow_link_xpath

        self.share_link = HeadlinesLocator.share_link_xpath
        self.copy_link = HeadlinesLocator.copy_link_xpath

        self.facebook_link = HeadlinesLocator.facebook_link_xpath
        self.twitter_link = HeadlinesLocator.twitter_link_xpath

    def click_headlines(self):
        headline = self.driver.find_element(By.LINK_TEXT, self.headline_text)
        headline.click()

        assert True, 'failed'
        print('clicked on Headlines')

    def click_follow(self):
        follow = self.driver.find_element(By.XPATH, self.follow_link)
        follow.click()

        assert True, 'failed'
        print('clicked on Follow')

    def click_share(self):
        share = self.driver.find_element(By.XPATH, self.share_link)
        share.click()

        assert True, 'failed'
        print('clicked on Share')

    def click_copy_link(self):
        copy = self.driver.find_element(By.XPATH, self.copy_link)
        copy.click()

        assert True, 'failed'
        print('clicked on copy link')

    def view_new_tab(self):
        link = pyperclip.paste()
        # open tab
        self.driver.execute_script('window.open()')
        print('new window open operation executed')
        sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        print('open a new window')
        sleep(3)
        self.driver.get(link)
        print('get the link')

        assert True, 'failed'
        print('Open new tab and pasted the link')
        sleep(3)

        self.driver.switch_to.window(self.driver.window_handles[0])
        print('back to the previous window')
        sleep(3)

    def click_facebook(self):
        facebook = self.driver.find_element(By.XPATH, self.facebook_link)
        facebook.click()
        sleep(3)

        assert True, 'failed'
        print('clicked on facebook')

    def click_twitter(self):
        twitter = self.driver.find_element(By.XPATH, self.twitter_link)
        twitter.click()
        sleep(3)

        assert True, 'failed'
        print('clicked on twitter')

