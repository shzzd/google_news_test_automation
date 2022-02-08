from time import sleep

from Selenium.Sample_project.GoogleNews.Locators.locators import HomePageLocator
from Selenium.Sample_project.GoogleNews.Pages.base_page import BasePage
from Selenium.Sample_project.GoogleNews.Pages.headlines_page import HeadlinesPage
from Selenium.Sample_project.GoogleNews.Pages.home_page import HomePage
from Selenium.Sample_project.GoogleNews.Tests.base_test import BaseTest


class TestCase3(BaseTest):
    # =================================================== Headlines ====================================================
    # click on follow
    def test_tc_1(self):
        BasePage(self.driver)

        # click Headlines
        HeadlinesPage(self.driver).click_headlines()
        sleep(3)

        # click Follow link
        HeadlinesPage(self.driver).click_follow()
        sleep(3)

    # copy link and paste in a new tab
    def test_tc_2(self):
        BasePage(self.driver)

        # click Headlines
        HeadlinesPage(self.driver).click_headlines()
        sleep(3)

        # click share link
        HeadlinesPage(self.driver).click_share()
        sleep(3)

        # click copy link
        HeadlinesPage(self.driver).click_copy_link()
        sleep(3)

        # open new tab and paste the link
        HeadlinesPage(self.driver).view_new_tab()
        sleep(5)

    # share the link on facebook
    def test_tc_3(self):
        BasePage(self.driver)

        # click Headlines
        HeadlinesPage(self.driver).click_headlines()
        sleep(3)

        # click share link
        HeadlinesPage(self.driver).click_share()
        sleep(3)

        # click facebook link
        HeadlinesPage(self.driver).click_facebook()
        sleep(3)

    # share the link on twitter
    def test_tc_4(self):
        BasePage(self.driver)

        # click Headlines
        HeadlinesPage(self.driver).click_headlines()
        sleep(3)

        # click share link
        HeadlinesPage(self.driver).click_share()
        sleep(3)

        # click twitter link
        HeadlinesPage(self.driver).click_twitter()
        sleep(3)

    # ================================================== News Title ====================================================
    # click a news title and save for later
    def test_tc_5(self):
        BasePage(self.driver)

        # click on a news title and save for later
        obj = HomePage(self.driver)
        obj.point_news_title_and_save(obj.news_title, obj.save_option)
        sleep(3)

    # click share, copy the link, open a new tab and paste
    def test_tc_6(self):
        BasePage(self.driver)

        # point title and click share
        obj = HomePage(self.driver)
        obj.point_news_title_and_share(obj.news_title, obj.share)
        sleep(3)

        # click copy link
        obj = HomePage(self.driver)
        obj.click_copy_link(obj.copy_link)
        sleep(3)

        # view new tab
        obj = HomePage(self.driver)
        obj.view_new_tab()
        sleep(5)

    # share on facebook
    def test_tc_7(self):
        BasePage(self.driver)

        # point title and click share
        obj = HomePage(self.driver)
        obj.point_news_title_and_share(obj.news_title, obj.share)
        sleep(3)

        # click facebook
        obj = HomePage(self.driver)
        obj.click_facebook(obj.facebook_icon)
        sleep(3)

    # share on twitter
    def test_tc_8(self):
        BasePage(self.driver)

        # point title and click share
        obj = HomePage(self.driver)
        obj.point_news_title_and_share(obj.news_title, obj.share)
        sleep(3)

        # click twitter
        obj = HomePage(self.driver)
        obj.click_twitter(obj.twitter_icon)
        sleep(3)

    # view full coverage
    def test_tc_9(self):
        BasePage(self.driver)

        # point title and click more icon
        HomePage(self.driver).point_news_title_and_more()
        sleep(3)

        # click view full coverage
        HomePage(self.driver).click_view_full_coverage()
        sleep(3)

    # go to ... page
    def test_tc_10(self):
        BasePage(self.driver)

        # point title and click more icon
        HomePage(self.driver).point_news_title_and_more()
        sleep(3)

        # click go to ... page
        HomePage(self.driver).click_go_to()
        sleep(3)

    # hide all stories
    def test_tc_11(self):
        BasePage(self.driver)

        # point title and click more icon
        HomePage(self.driver).point_news_title_and_more()
        sleep(3)

        # click hide all stories
        HomePage(self.driver).click_hide_stories()
        sleep(3)

    # more stories
    def test_tc_12(self):
        BasePage(self.driver)

        # point title and click more icon
        HomePage(self.driver).point_news_title_and_more()
        sleep(3)

        # click more stories
        HomePage(self.driver).click_more_stories()
        sleep(3)

    # fewer stories
    def test_tc_13(self):
        BasePage(self.driver)

        # point title and click more icon
        HomePage(self.driver).point_news_title_and_more()
        sleep(3)

        # click fewer stories
        HomePage(self.driver).click_fewer_stories()
        sleep(3)

    # ==================================================== Weather =====================================================
    # celsius
    def test_tc_14(self):
        BasePage(self.driver)

        # click on C
        HomePage(self.driver).click_celsius()
        sleep(3)

    # fahrenheit
    def test_tc_15(self):
        BasePage(self.driver)

        # click on F
        HomePage(self.driver).click_fahrenheit()
        sleep(3)

    # K
    def test_tc_16(self):
        BasePage(self.driver)

        # click on K
        HomePage(self.driver).click_k()
        sleep(3)

    # more on weather.com
    def test_tc_17(self):
        BasePage(self.driver)

        # click on more on weather.com
        HomePage(self.driver).click_more_on_weather()
        sleep(3)

    # ================================================== Fact Check ====================================================
    # click a news title and save for later
    def test_tc_18(self):
        BasePage(self.driver)

        # click on a news title and save for later
        obj = HomePage(self.driver)
        obj.point_news_title_and_save(obj.news_title_fact, obj.save_option_fact)
        sleep(3)

    # click share, copy the link, open a new tab and paste
    def test_tc_19(self):
        BasePage(self.driver)

        # point title and click share
        obj = HomePage(self.driver)
        obj.point_news_title_and_share(obj.news_title_fact, obj.share_fact)
        sleep(3)

        # click copy link
        obj.click_copy_link(obj.copy_link)
        sleep(3)

        # view new tab
        obj.view_new_tab()
        sleep(5)

    # share on facebook
    def test_tc_20(self):
        BasePage(self.driver)

        # point title and click share
        obj = HomePage(self.driver)
        obj.point_news_title_and_share(obj.news_title_fact, obj.share_fact)
        sleep(3)

        # click facebook
        obj.click_facebook(obj.facebook_icon)
        sleep(3)

    # share on twitter
    def test_tc_21(self):
        BasePage(self.driver)

        # point title and click share
        obj = HomePage(self.driver)
        obj.point_news_title_and_share(obj.news_title_fact, obj.share_fact)
        sleep(3)

        # click twitter
        obj.click_twitter(obj.twitter_icon)
        sleep(3)

    # view full coverage
    def test_tc_22(self):
        BasePage(self.driver)

        # point title and click more icon
        HomePage(self.driver).point_news_title_and_more()
        sleep(3)

        # click view full coverage
        HomePage(self.driver).click_view_full_coverage()
        sleep(3)

    # go to ... page
    def test_tc_23(self):
        BasePage(self.driver)

        # point title and click more icon
        HomePage(self.driver).point_news_title_and_more()
        sleep(3)

        # click view full coverage
        HomePage(self.driver).click_go_to()
        sleep(3)

    # hide all stories
    def test_tc_24(self):
        BasePage(self.driver)

        # point title and click more icon
        HomePage(self.driver).point_news_title_and_more()
        sleep(3)

        # click view full coverage
        HomePage(self.driver).click_hide_stories()
        sleep(3)

    # more stories
    def test_tc_25(self):
        BasePage(self.driver)

        # point title and click more icon
        HomePage(self.driver).point_news_title_and_more()
        sleep(3)

        # click view full coverage
        HomePage(self.driver).click_more_stories()
        sleep(3)

    # fewer stories
    def test_tc_26(self):
        BasePage(self.driver)

        # point title and click more icon
        HomePage(self.driver).point_news_title_and_more()
        sleep(3)

        # click view full coverage
        HomePage(self.driver).click_fewer_stories()
        sleep(3)

    # ================================================ Beyond Headlines ================================================
    # save beyond headlines news
    def test_tc_27(self):
        BasePage(self.driver)

        # beyond headlines point news title and save
        obj = HomePage(self.driver)
        obj.point_news_title_and_save(obj.beyond_headlines_news, obj.beyond_headlines_save)
        sleep(3)

    # click share, copy the link, open a new tab and paste
    def test_tc_28(self):
        BasePage(self.driver)

        # point title and click share
        obj = HomePage(self.driver)
        obj.point_news_title_and_share(obj.beyond_headlines_news, obj.beyond_headlines_share)
        sleep(3)

        # click copy link
        obj.click_copy_link(obj.copy_link)
        sleep(3)

        # view new tab
        obj.view_new_tab()
        sleep(5)

    # share on facebook
    def test_tc_29(self):
        BasePage(self.driver)

        # point title and click share
        obj = HomePage(self.driver)
        obj.point_news_title_and_share(obj.beyond_headlines_news, obj.beyond_headlines_share)
        sleep(3)

        # click facebook
        obj.click_facebook(obj.facebook_icon)
        sleep(3)

    # share on twitter
    def test_tc_30(self):
        BasePage(self.driver)

        # point title and click share
        obj = HomePage(self.driver)
        obj.point_news_title_and_share(obj.beyond_headlines_news, obj.beyond_headlines_share)
        sleep(3)

        # click twitter
        obj.click_twitter(obj.twitter_icon)
        sleep(3)

    # ================================================== In the news ===================================================
    # go to In the news and click any tag
    def test_tc_31(self):
        BasePage(self.driver)

        # point in the news and click a tag
        obj = HomePage(self.driver)
        obj.click_tag_in_the_news(obj.tag_in_the_news, obj.tag_name)
        sleep(3)
