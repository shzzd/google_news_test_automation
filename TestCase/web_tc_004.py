from time import sleep

from Selenium.Sample_project.GoogleNews.Pages.base_page import BasePage
from Selenium.Sample_project.GoogleNews.Tests.base_test import BaseTest
from Selenium.Sample_project.GoogleNews.Pages.home_page import HomePage


class TestCase4(BaseTest):
    # =================================================== For You ======================================================
    # click a news title and save for later
    def test_tc_1(self):
        BasePage(self.driver)

        # click on For you
        obj = HomePage(self.driver)
        obj.click_for_you(obj.for_you_link)

        # click on a news title and save for later
        obj.point_news_title_and_save(obj.news_title_for_you, obj.save_option_for_you)
        sleep(3)

    # click share, copy the link, open a new tab and paste
    def test_tc_2(self):
        BasePage(self.driver)

        # click on For you
        obj = HomePage(self.driver)
        obj.click_for_you(obj.for_you_link)

        # point title and click share
        obj.point_news_title_and_share(obj.news_title_for_you, obj.share_for_you)
        sleep(3)

        # click copy link
        obj.click_copy_link(obj.copy_link)
        sleep(3)

        # view new tab
        obj.view_new_tab()
        sleep(5)

    # share on facebook
    def test_tc_3(self):
        BasePage(self.driver)

        # click on For you
        obj = HomePage(self.driver)
        obj.click_for_you(obj.for_you_link)

        # point title and click share
        obj.point_news_title_and_share(obj.news_title_for_you, obj.share_for_you)
        sleep(3)

        # click facebook
        obj.click_facebook(obj.facebook_icon)
        sleep(3)

    # share on twitter
    def test_tc_4(self):
        BasePage(self.driver)

        # click on For you
        obj = HomePage(self.driver)
        obj.click_for_you(obj.for_you_link)

        # point title and click share
        obj.point_news_title_and_share(obj.news_title_for_you, obj.share_for_you)
        sleep(3)

        # click twitter
        obj.click_twitter(obj.twitter_icon)
        sleep(3)

    # view full coverage
    def test_tc_5(self):
        BasePage(self.driver)

        # click on For you
        obj = HomePage(self.driver)
        obj.click_for_you(obj.for_you_link)

        # point title and click more icon
        obj.point_news_title_and_more(obj.news_title_for_you, obj.more_icon_for_you)
        sleep(3)

        # click view full coverage
        obj.click_view_full_coverage()
        sleep(3)

    # go to ... page
    def test_tc_6(self):
        BasePage(self.driver)

        # click on For you
        obj = HomePage(self.driver)
        obj.click_for_you(obj.for_you_link)

        # point title and click more icon
        obj.point_news_title_and_more()
        sleep(3)

        # click go to ... page
        HomePage(self.driver).click_go_to()
        sleep(3)

    # hide all stories
    def test_tc_7(self):
        BasePage(self.driver)

        # click on For you
        obj = HomePage(self.driver)
        obj.click_for_you(obj.for_you_link)

        # point title and click more icon
        obj.point_news_title_and_more()
        sleep(3)

        # click hide all stories
        HomePage(self.driver).click_hide_stories()
        sleep(3)

    # more stories
    def test_tc_8(self):
        BasePage(self.driver)

        # click on For you
        obj = HomePage(self.driver)
        obj.click_for_you(obj.for_you_link)

        # point title and click more icon
        obj = HomePage(self.driver)
        obj.point_news_title_and_more()
        sleep(3)

        # click more stories
        obj.click_more_stories()
        sleep(3)

    # fewer stories
    def test_tc_9(self):
        BasePage(self.driver)

        # click on For you
        obj = HomePage(self.driver)
        obj.click_for_you(obj.for_you_link)

        # point title and click more icon
        obj = HomePage(self.driver)
        obj.point_news_title_and_more()
        sleep(3)

        # click fewer stories
        obj.click_fewer_stories()
        sleep(3)
