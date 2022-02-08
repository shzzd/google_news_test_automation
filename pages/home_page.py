import pyperclip
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from Selenium.Sample_project.GoogleNews.Locators.locators import *
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        # News Title ----====----
        self.news_title = HomePageLocator.news_title_xpath
        self.save_option = HomePageLocator.save_option_xpath
        self.share = HomePageLocator.share_link_xpath
        self.more_icon = HomePageLocator.more_icon_xpath

        # self.view_full_coverage = HomePages.view_full_coverage_xpath
        # self.go_to = HomePages.go_to_xpath
        # self.hide_stories = HomePages.hide_all_xpath
        # self.more_stories = HomePages.more_stories_xpath
        # self.fewer_stories = HomePages.fewer_stories_xpath

        # Fact Check ----====----
        self.news_title_fact = HomePageLocator.news_title_fact_xpath
        self.save_option_fact = HomePageLocator.save_fact_xpath
        self.share_fact = HomePageLocator.share_link_fact_xpath
        self.more_icon_fact = HomePageLocator.more_icon_fact_xpath

        # self.view_full_coverage_face = HomePages.view_full_coverage_face_xpath
        # self.hide_stories_face = HomePages.hide_all_face_xpath
        # self.more_stories_face = HomePages.more_stories_face_xpath
        # self.fewer_stories_face = HomePages.fewer_stories_face_xpath

        # Beyond Headlines News Title ----====----
        self.beyond_headlines_news = HomePageLocator.beyond_headlines_news_title_xpath
        self.beyond_headlines_save = HomePageLocator.beyond_headlines_save_xpath
        self.beyond_headlines_share = HomePageLocator.beyond_headlines_share__xpath

        # For You ----====----
        self.for_you_text = ForYouPageLocator.for_you_text_xpath
        self.for_you_link = ForYouPageLocator.for_you_link_xpath
        self.news_title_for_you = ForYouPageLocator.news_title_for_you_xpath
        self.save_option_for_you = ForYouPageLocator.save_for_you_xpath
        self.share_for_you = ForYouPageLocator.share_for_you_xpath
        self.more_icon_for_you = ForYouPageLocator.more_for_you_xpath

        # self.view_full_coverage = ForYouPageLocator.view_full_coverage_xpath
        # self.go_to = ForYouPageLocator.go_to_xpath
        # self.hide_stories = ForYouPageLocator.hide_all_xpath
        # self.more_stories = ForYouPageLocator.more_stories_xpath
        # self.fewer_stories = ForYouPageLocator.fewer_stories_xpath

        # Fact Check, News Title, Beyond the Headlines, For you, Covid-Int'l -> copy_link, facebook_link, twitter_link
        self.copy_link = HomePageLocator.copy_link_icon_xpath
        self.facebook_icon = HomePageLocator.facebook_icon_xpath
        self.twitter_icon = HomePageLocator.twitter_icon_xpath

        # Weather ----====----
        self.celsius = HomePageLocator.celsius_xpath
        self.fahrenheit = HomePageLocator.fahrenheit_xpath
        self.k = HomePageLocator.k_xpath
        self.more_on_weather = HomePageLocator.more_on_weather_xpath

        # In the news ----====----
        self.in_the_news = HomePageLocator.in_the_news_xpath
        self.tag_in_the_news = HomePageLocator.tag_in_the_news_xpath
        self.tag_name = HomePageLocator.tag_name_xpath

    # For You
    def click_for_you(self, for_you):
        for_you_link = self.driver.find_element(By.XPATH, for_you)
        for_you_link.click()

        assert True, 'failed'
        print('Clicked on For you')
        sleep(3)

    # News Title, Beyond the Headlines, Fact Check, For you
    def point_news_title_and_save(self, news, save):
        news_title = self.driver.find_element(By.XPATH, news)
        save_option = self.driver.find_element(By.XPATH, save)

        actions = ActionChains(self.driver)
        actions.move_to_element(news_title).move_to_element(save_option).click().perform()

        assert True, 'failed'
        print('The news saved successfully')
        sleep(3)

    def point_news_title_and_share(self, news, share):
        news_title = self.driver.find_element(By.XPATH, news)
        share = self.driver.find_element(By.XPATH, share)

        actions = ActionChains(self.driver)
        actions.move_to_element(news_title).move_to_element(share).click().perform()

        assert True, 'failed'
        print('Clicked on share')
        sleep(3)

    def click_copy_link(self, copy_link):
        copy = self.driver.find_element(By.XPATH, copy_link)
        copy.click()

        assert True, 'failed'
        print('clicked on copy link')
        sleep(3)

    def view_new_tab(self):
        link = pyperclip.paste()
        # open tab
        self.driver.execute_script('window.open()')
        print('new window open operation executed')
        sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        print('open a new window')

        self.driver.get(link)
        print('get the link')

        assert True, 'failed'
        print('The link open on new tab successfully')
        sleep(3)

        self.driver.switch_to.window(self.driver.window_handles[0])
        print('back to the previous window')
        sleep(3)

    def click_facebook(self, facebook_icon):
        facebook = self.driver.find_element(By.XPATH, facebook_icon)
        facebook.click()

        assert True, 'failed'
        print('clicked on facebook')
        sleep(3)

    def click_twitter(self, twitter_icon):
        twitter = self.driver.find_element(By.XPATH, twitter_icon)
        twitter.click()

        assert True, 'failed'
        print('clicked on twitter')
        sleep(3)

    def point_news_title_and_more(self, news, more_icon):
        news_title = self.driver.find_element(By.XPATH, news)
        more = self.driver.find_element(By.XPATH, more_icon)
        more.click()
        sleep(3)

        actions = ActionChains(self.driver)
        actions.move_to_element(news_title).move_to_element(more).click().perform()

        assert True, 'failed'
        print('clicked on more icon')
        sleep(3)

    def click_view_full_coverage(self, view):
        view_full = self.driver.find_element(By.XPATH, view)
        view_full.click()

        assert True, 'failed'
        print('clicked on view full coverage')
        sleep(3)

    def click_go_to(self, go):
        go_to = self.driver.find_element(By.XPATH, go)
        go_to.click()

        assert True, 'failed'
        print('clicked on go to')
        sleep(3)

    def click_hide_stories(self, hide):
        hide_stories = self.driver.find_element(By.XPATH, hide)
        hide_stories.click()

        assert True, 'failed'
        print('clicked on hide stories')
        sleep(3)

    def click_more_stories(self, more_s):
        more_stories = self.driver.find_element(By.XPATH, more_s)
        more_stories.click()

        assert True, 'failed'
        print('clicked on more stories')
        sleep(3)

    def click_fewer_stories(self, fewer_s):
        fewer_stories = self.driver.find_element(By.XPATH, fewer_s)
        fewer_stories.click()

        assert True, 'failed'
        print('clicked on fewer stories')
        sleep(3)

    # Weather
    def click_celsius(self):
        celsius = self.driver.find_element(By.XPATH, self.celsius)
        celsius.click()

        assert True, 'failed'
        print('clicked on celsius')
        sleep(3)

    def click_fahrenheit(self):
        fahrenheit = self.driver.find_element(By.XPATH, self.fahrenheit)
        fahrenheit.click()

        assert True, 'failed'
        print('clicked on fahrenheit')
        sleep(3)

    def click_k(self):
        k = self.driver.find_element(By.XPATH, self.k)
        k.click()

        assert True, 'failed'
        print('clicked on k')
        sleep(3)

    def click_more_on_weather(self):
        more_on_weather = self.driver.find_element(By.XPATH, self.more_on_weather)
        more_on_weather.click()

        assert True, 'failed'
        print('clicked on more on weather.com')
        sleep(3)

    # In the news
    def click_tag_in_the_news(self, in_the_news_tag, tag_name):
        tag_in_the_news = self.driver.find_element(By.XPATH, in_the_news_tag)
        tag_in_the_news.click()
        sleep(3)

        tag = self.driver.find_element(By.XPATH, tag_name)

        assert True, 'failed'
        print(f'Clicked on {tag.text} tag')
        sleep(3)

    # # Fact Check
    # def point_news_title_save(self, news, save):
    #     news_title = self.driver.find_element(By.XPATH, news)
    #     save_option = self.driver.find_element(By.XPATH, save)
    #
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(news_title).move_to_element(save_option).click().perform()
    #
    #     assert True, 'failed'
    #     print('The news saved successfully')
    #     sleep(3)
    #
    # def point_news_title_and_share(self):
    #     news_title = self.driver.find_element(By.XPATH, self.news_title)
    #     share = self.driver.find_element(By.XPATH, self.share)
    #
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(news_title).move_to_element(share).click().perform()
    #
    #     assert True, 'failed'
    #     print('Clicked on share')
    #     sleep(3)
    #
    # def click_copy_link(self):
    #     copy = self.driver.find_element(By.XPATH, self.copy_link)
    #     copy.click()
    #
    #     assert True, 'failed'
    #     print('clicked on copy link')
    #     sleep(3)
    #
    # def view_new_tab(self):
    #     link = pyperclip.paste()
    #     # open tab
    #     self.driver.execute_script('window.open()')
    #     print('window open')
    #     sleep(3)
    #     self.driver.switch_to.window(self.driver.window_handles[1])
    #     print('handle window')
    #     sleep(3)
    #     self.driver.get(link)
    #     print('get the link')
    #
    #     assert True, 'failed'
    #     print('The link open on new tab successfully')
    #     sleep(3)
    #
    # def click_facebook(self):
    #     facebook = self.driver.find_element(By.XPATH, self.facebook_icon)
    #     facebook.click()
    #
    #     assert True, 'failed'
    #     print('clicked on facebook')
    #     sleep(3)
    #
    # def click_twitter(self):
    #     twitter = self.driver.find_element(By.XPATH, self.twitter_icon)
    #     twitter.click()
    #
    #     assert True, 'failed'
    #     print('clicked on twitter')
    #     sleep(3)
    #
    # def point_news_title_and_more(self):
    #     news_title = self.driver.find_element(By.XPATH, self.news_title)
    #     more = self.driver.find_element(By.XPATH, self.more_icon)
    #     more.click()
    #     sleep(3)
    #
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(news_title).move_to_element(more).click().perform()
    #
    #     assert True, 'failed'
    #     print('clicked on more icon')
    #     sleep(3)
    #
    # def click_view_full_coverage(self):
    #     view_full = self.driver.find_element(By.XPATH, self.view_full_coverage)
    #     view_full.click()
    #
    #     assert True, 'failed'
    #     print('clicked on view full coverage')
    #     sleep(3)
    #
    # def click_go_to(self):
    #     go_to = self.driver.find_element(By.XPATH, self.go_to)
    #     go_to.click()
    #
    #     assert True, 'failed'
    #     print('clicked on go to')
    #     sleep(3)
    #
    # def click_hide_stories(self):
    #     hide_stories = self.driver.find_element(By.XPATH, self.hide_stories)
    #     hide_stories.click()
    #
    #     assert True, 'failed'
    #     print('clicked on hide stories')
    #     sleep(3)
    #
    # def click_more_stories(self):
    #     more_stories = self.driver.find_element(By.XPATH, self.more_stories)
    #     more_stories.click()
    #
    #     assert True, 'failed'
    #     print('clicked on more stories')
    #     sleep(3)
    #
    # def click_fewer_stories(self):
    #     fewer_stories = self.driver.find_element(By.XPATH, self.fewer_stories)
    #     fewer_stories.click()
    #
    #     assert True, 'failed'
    #     print('clicked on fewer stories')
    #     sleep(3)