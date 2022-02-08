'''
3/2 = 8.44 -
4/2 = 9.10 -
5/2 = 8.20 - 5.00
6/2 = 8.14
'''


class SearchPageLocator:

    # google text
    google_text_css = "/html[1]/body[1]/div[4]/header[1]/div[2]/div[1]/div[4]/div[1]/a[1]/span[1]"

    # search_page objects
    search_box_css = "/html[1]/body[1]/div[4]/header[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/\
                        div[1]/div[1]/input[2]"

    # featured topic
    featured_topic_box_css = "/html[1]/body[1]/div[4]/header[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/\
                                div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]"

    # feature topic name
    featured_topic_name_css = "/html[1]/body[1]/c-wiz[2]/div[1]/div[2]/c-wiz[1]/div[1]/div[1]/div[1]/div[1]/div[2]/\
                                h2[1]"

    # news box
    news_box_css = "/html[1]/body[1]/div[4]/header[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/\
                    div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]"

    # news name
    news_name_css = "body.tQj5Y.ghyPEc.IqBfM.ecJEib.EWZcud.lF2Cpe.k1PYFe.dm7YTc.gb_he.hZmmCc.rrkuMc.EIlDfe.cjGgHb.\
                    d8Etdd.LcUz9d:nth-child(2) c-wiz.zQTmif.SSPGKf:nth-child(29) div.T4LgNb:nth-child(1) div.FVeGwb.\
                    NLCVwf.bWfURe c-wiz.MNK4Vd:nth-child(2) div.XCz6Hb.rHXK0e.cd29Sd.tXqPBe div.giq3T div.apU4O div.\
                    xMjzl > h2.OJMBqe"


class HeadlinesLocator:

    headline_text_link_text = 'Headlines'
    follow_link_xpath = '//body/c-wiz[2]/div[1]/div[2]/c-wiz[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]'
    share_link_xpath = '//body/c-wiz[2]/div[1]/div[2]/c-wiz[1]/div[1]/div[1]/div[2]/div[2]/span[1]/div[1]'
    copy_link_xpath = "//span[contains(text(),'link')]"
    facebook_link_xpath = '//body/div[12]/div[2]/div[1]/div[1]/div[3]/div[2]/div[2]/button[1]'
    twitter_link_xpath = '//body/div[12]/div[2]/div[1]/div[1]/div[3]/div[2]/div[3]/button[1]/*[1]'


class HomePageLocator:

    # News Title
    news_title_xpath = '//body/c-wiz[1]/div[1]/div[2]/div[2]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/div[3]/div[1]/\
                        div[1]/article[1]/a[1]'
    save_option_xpath = '//body/c-wiz[1]/div[1]/div[2]/div[2]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/div[3]/div[1]/\
                        div[1]/article[1]/div[1]/menu[1]/div[1]/div[1]'
    share_link_xpath = '//body/c-wiz[1]/div[1]/div[2]/div[2]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/div[3]/div[1]/\
                        div[1]/article[1]/div[1]/menu[1]/span[1]/div[1]'
    more_icon_xpath = '//body/c-wiz[1]/div[1]/div[2]/div[2]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/div[3]/div[1]/div[1]/\
                        article[1]/div[1]/menu[1]/span[2]/div[1]'

    # News title problem (start)
    view_full_coverage_xpath = '//*[@id="yDmH0d"]/div[13]/div/div/span[1]'
    go_to_xpath = '//body/div[14]/div[1]/div[1]/span[2]'
    hide_all_xpath = "//div[contains(text(),'Hide all stories from CNN')]"
    more_stories_xpath = "//div[contains(text(),'More stories like this')]"
    fewer_stories_xpath = "//div[contains(text(),'Fewer stories like this')]"
    # end

    # Fact Check
    news_title_fact_xpath = '//body/c-wiz[1]/div[1]/div[2]/div[2]/div[1]/aside[1]/c-wiz[1]/div[1]/div[2]/div[1]/div[2]/\
                            article[1]/a[1]'
    save_fact_xpath = '//body/c-wiz[1]/div[1]/div[2]/div[2]/div[1]/aside[1]/c-wiz[1]/div[1]/div[2]/div[1]/div[2]/\
                        article[1]/div[1]/menu[1]/div[1]/div[1]'
    share_link_fact_xpath = '//body/c-wiz[1]/div[1]/div[2]/div[2]/div[1]/aside[1]/c-wiz[1]/div[1]/div[2]/div[1]/div[2]/\
                            article[1]/div[1]/menu[1]/span[1]/div[1]'
    more_icon_fact_xpath = '//body/c-wiz[1]/div[1]/div[2]/div[2]/div[1]/aside[1]/c-wiz[1]/div[1]/div[2]/div[1]/div[2]/\
                            article[1]/div[1]/menu[1]/span[2]/div[1]'

    # News title problem (start)
    # view_full_coverage_fact_xpath = "//div[contains(text(),'Go to PolitiFact')]"
    # hide_all_fact_xpath = "/html[1]/body[1]/div[14]/div[1]/div[1]/span[2]/div[3]/div[1]/div[1]"
    # more_stories_fact_xpath = "//div[contains(text(),'More stories like this')]"
    # fewer_stories_fact_xpath = "//div[contains(text(),'Fewer stories like this')]"
    # end

    # Beyond the headlines
    beyond_headlines_news_title_xpath = '//body/c-wiz[1]/div[1]/div[2]/div[2]/div[1]/aside[1]/c-wiz[1]/div[1]/div[3]/\
                                        div[1]/div[2]/article[1]/a[1]'
    beyond_headlines_save_xpath = '//body/c-wiz[1]/div[1]/div[2]/div[2]/div[1]/aside[1]/c-wiz[1]/div[1]/div[3]/div[1]/\
                                    div[2]/article[1]/div[1]/menu[1]/div[1]/div[1]'
    beyond_headlines_share__xpath = '//body/c-wiz[1]/div[1]/div[2]/div[2]/div[1]/aside[1]/c-wiz[1]/div[1]/div[3]/div[1]\
                                    /div[2]/article[1]/div[1]/menu[1]/span[1]/div[1]'

    # Weather
    celsius_xpath = "//button[contains(text(),'C')]"
    fahrenheit_xpath = "//button[contains(text(),'F')]"
    k_xpath = "//button[contains(text(),'K')]"
    more_on_weather_xpath = "//a[contains(text(),'More on weather.com')]"

    # All share icon
    copy_link_icon_xpath = "//span[contains(text(),'link')]"
    facebook_icon_xpath = "//div[contains(text(),'Facebook')]"
    twitter_icon_xpath = "//div[contains(text(),'Twitter')]"

    # In the news
    in_the_news_xpath = "//h2[contains(text(),'In the news')]"
    tag_in_the_news_xpath = '//body/c-wiz[1]/div[1]/div[2]/div[2]/div[1]/aside[1]/c-wiz[1]/div[1]/div[5]/div[1]/div[2]\
                            /div[1]/a[1]'
    tag_name_xpath = '/html[1]/body[1]/c-wiz[2]/div[1]/div[2]/c-wiz[1]/div[1]/div[1]/div[1]/div[1]/div[2]/h2[1]'


class ForYouPageLocator:
    for_you_text_xpath = '//header/div[4]/div[2]/div[1]/c-wiz[1]/div[1]/div[2]/a[1]'

    for_you_link_xpath = "//span[contains(text(),'For you')]"

    news_title_for_you_xpath = '//body/c-wiz[2]/div[1]/div[2]/div[2]/div[1]/main[1]/div[1]/c-wiz[1]/div[1]/div[2]/\
                                div[1]/article[1]/a[1]'
    save_for_you_xpath = '//body/c-wiz[2]/div[1]/div[2]/div[2]/div[1]/main[1]/div[1]/c-wiz[1]/div[1]/div[2]/div[1]/\
                            article[1]/div[1]/menu[1]/div[1]/div[1]'
    share_for_you_xpath = '//body/c-wiz[2]/div[1]/div[2]/div[2]/div[1]/main[1]/div[1]/c-wiz[1]/div[1]/div[2]/div[1]/\
                            article[1]/div[1]/menu[1]/span[1]/div[1]'
    more_for_you_xpath = '//body/c-wiz[2]/div[1]/div[2]/div[2]/div[1]/main[1]/div[1]/c-wiz[1]/div[1]/div[2]/div[1]/\
                            article[1]/div[1]/menu[1]/span[2]/div[1]'

    # News title problem (start)
    # view_full_coverage_fact_xpath = "//div[contains(text(),'Go to PolitiFact')]"
    # hide_all_fact_xpath = "/html[1]/body[1]/div[14]/div[1]/div[1]/span[2]/div[3]/div[1]/div[1]"
    # more_stories_fact_xpath = "//div[contains(text(),'More stories like this')]"
    # fewer_stories_fact_xpath = "//div[contains(text(),'Fewer stories like this')]"
    # end


class CovidLocator:
    covid_link_xpath = '//header/div[4]/div[2]/div[1]/c-wiz[1]/div[1]/div[5]/div[2]/a[1]/div[2]/span[1]'

    # Latest
    latest_covid_xpath = "//span[contains(text(),'Latest')]"
    latest_news_covid_xpath = '//body/c-wiz[2]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[1]/div[1]/div[1]/\
                                    main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/article[1]/a[1]'

    # Local
    local_covid_xpath = '//body[1]/c-wiz[2]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[1]/div[2]/div[2]/span[1]/div[1]/\
                        div[1]/span[1]'
    location_covid_xpath = "/html[1]/body[1]/c-wiz[2]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[2]/div[1]/\
                            div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/\
                            div[1]/div[2]/div[1]/div[1]"

    # International
    international_covid_xpath = "//span[contains(text(),'International')]"

    news_title_covid_xpath = '//body/c-wiz[2]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[3]/div[1]/div[1]/\
                                main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[2]/div[1]/div[2]/article[1]/a[1]'

    # all
    def __init__(self, i):
        self.i = i

        # save, share and more
        self.save_covid_xpath = f'//body/c-wiz[2]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/\
                                    div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[{self.i}]/div[1]/\
                                    div[2]/article[1]/div[1]/menu[1]/div[1]/div[1]'
        self.share_covid_xpath = f'//body/c-wiz[2]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/\
                                    div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[{self.i}]/div[1]/div[2]/\
                                    article[1]/div[1]/menu[1]/span[2]/div[1]'
        self.more_covid_xpath = f'//body/c-wiz[2]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/\
                                div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[{self.i}]/div[1]/div[2]/\
                                article[1]/div[1]/menu[1]/span[3]/div[1]'

        # News title problem (start)
        # view_full_coverage_covid_xpath = "//div[contains(text(),'Go to PolitiFact')]"
        # hide_all_covid_xpath = "/html[1]/body[1]/div[14]/div[1]/div[1]/span[2]/div[3]/div[1]/div[1]"
        # more_stories_covid_xpath = "//div[contains(text(),'More stories like this')]"
        # fewer_stories_covid_xpath = "//div[contains(text(),'Fewer stories like this')]"
        # end


class UsLocator:
    us_xpath = "//span[contains(text(),'U.S.')]"

    news_title_us_xpath = '//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/\
                            main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/a[1]'
    save_us_xpath = '//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/\
                    main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/div[1]/div[1]'
    share_us_xpath = '//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/\
                    main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/span[1]/div[1]'
    more_us_xpath = '//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/\
                    main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/span[2]/div[1]'

    # News title problem (start)
    # view_full_coverage_us_xpath = "//div[contains(text(),'View Full Coverage')]"
    # go_to_us_xpath = '//div[contains(text(),'Go to Fox News')]'
    # hide_all_us_xpath = "//div[contains(text(),'Hide all stories from Fox News')]"
    # more_stories_us_xpath = "//div[contains(text(),'More stories like this')]"
    # fewer_stories_us_xpath = "//div[contains(text(),'Fewer stories like this')]"
    # end done


class WorldLocator:
    world_xpath = '//header/div[4]/div[2]/div[1]/c-wiz[1]/div[1]/div[5]/div[5]/a[1]'

    news_title_world_xpath = '//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[1]/main[1]/c-wiz[1]/div[1]/\
                            div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/a[1]'
    save_world_xpath = '//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/\
                        main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/div[1]/div[1]'
    share_world_xpath = '//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/\
                        main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/span[1]/div[1]'
    more_world_xpath = '//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/\
                        main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/span[2]/div[1]'

    # News title problem (start)
    # view_full_coverage_world_xpath = "//div[contains(text(),'View Full Coverage')]"
    # go_to_us_xpath = '//div[contains(text(),'Go to The Washington Post')]'
    # hide_all_world_xpath = "//div[contains(text(),'Hide all stories from The Washington Post')]"
    # more_stories_world_xpath = "//div[contains(text(),'More stories like this')]"
    # fewer_stories_world_xpath = "//div[contains(text(),'Fewer stories like this')]"
    # end


class YourLocalNewsLocator:
    your_local_news_xpath = "//span[contains(text(),'Your local news')]"

    news_your_local_xpath = '//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[1]/div[1]/div[1]/main[1]/\
                            c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/article[1]/a[1]'
    save_your_local_xpath = '//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[1]/div[1]/div[1]/main[1]/\
                            c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/div[1]/div[1]'
    share_your_local_xpath = '//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[1]/div[1]/div[1]/\
                main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/span[1]/div[1]'
    more_your_local_xpath = '//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[1]/div[1]/div[1]/main[1]/\
                        c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/span[2]/div[1]'

    # News title problem (start)
    # view_full_coverage_your_local_xpath = "//div[contains(text(),'Go to The Daily Star')]"
    # hide_all_your_local_xpath = "//div[contains(text(),'Hide all stories from The Daily Star')]"
    # more_stories_your_local_xpath = "//div[contains(text(),'More stories like this')]"
    # fewer_stories_your_local_xpath = "//div[contains(text(),'Fewer stories like this')]"
    # end done


class BusinessLocator:
    business_xpath = "//span[contains(text(),'Business')]"

    # all
    def __init__(self, i):
        self.i = i

        self.news_business_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/a[1]'
        self.save_business_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/div[1]/div[1]'
        self.share_business_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/span[1]/div[1]'
        self.more_business_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/span[2]/div[1]'

        # News title problem (start)
        # view_full_coverage_business_xpath = "//div[contains(text(),'Go to PolitiFact')]"
        # hide_all_business_xpath = "/html[1]/body[1]/div[14]/div[1]/div[1]/span[2]/div[3]/div[1]/div[1]"
        # more_stories_business_xpath = "//div[contains(text(),'More stories like this')]"
        # fewer_stories_business_xpath = "//div[contains(text(),'Fewer stories like this')]"
        # end


class TechnologyLocator:
    technology_xpath = "//span[contains(text(),'Technology')]"

    # all
    def __init__(self, i):
        self.i = i

        self.news_technology_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/a[1]'
        self.save_technology_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/div[1]/div[1]'
        self.share_technology_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/span[1]/div[1]'
        self.more_technology_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/span[2]/div[1]'

        # News title problem (start)
        # view_full_coverage_technology_xpath = "//div[contains(text(),'Go to PolitiFact')]"
        # hide_all_technology_xpath = "/html[1]/body[1]/div[14]/div[1]/div[1]/span[2]/div[3]/div[1]/div[1]"
        # more_stories_technology_xpath = "//div[contains(text(),'More stories like this')]"
        # fewer_stories_technology_xpath = "//div[contains(text(),'Fewer stories like this')]"
        # end


class EntertainmentLocator:
    entertainment_xpath = "//span[contains(text(),'Entertainment')]"

    # all
    def __init__(self, i):
        self.i = i

        self.news_entertainment_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/a[1]'
        self.save_entertainment_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/div[1]/div[1]'
        self.share_entertainment_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/span[1]/div[1]'
        self.more_entertainment_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/span[2]/div[1]'

        # News title problem (start)
        # view_full_coverage_entertainment_xpath = "//div[contains(text(),'Go to PolitiFact')]"
        # hide_all_entertainment_xpath = "/html[1]/body[1]/div[14]/div[1]/div[1]/span[2]/div[3]/div[1]/div[1]"
        # more_stories_entertainment_xpath = "//div[contains(text(),'More stories like this')]"
        # fewer_stories_entertainment_xpath = "//div[contains(text(),'Fewer stories like this')]"
        # end


class SportsLocator:
    sports_xpath = "//span[contains(text(),'Sports')]"

    # all
    def __init__(self, i):
        self.i = i

        self.news_sports_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/a[1]'
        self.save_sports_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/div[1]/div[1]'
        self.share_sports_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/span[1]/div[1]'
        self.more_sports_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/span[2]/div[1]'

        # News title problem (start)
        # view_full_coverage_sports_xpath = "//div[contains(text(),'Go to PolitiFact')]"
        # hide_all_sports_xpath = "/html[1]/body[1]/div[14]/div[1]/div[1]/span[2]/div[3]/div[1]/div[1]"
        # more_stories_sports_xpath = "//div[contains(text(),'More stories like this')]"
        # fewer_stories_sports_xpath = "//div[contains(text(),'Fewer stories like this')]"
        # end


class ScienceLocator:
    science_xpath = "//span[contains(text(),'Science')]"

    # all
    def __init__(self, i):
        self.i = i

        self.news_science_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/a[1]'
        self.save_science_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/div[1]/div[1]'
        self.share_science_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/span[1]/div[1]'
        self.more_science_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/span[2]/div[1]'

        # News title problem (start)
        # view_full_coverage_science_xpath = "//div[contains(text(),'Go to PolitiFact')]"
        # hide_all_science_xpath = "/html[1]/body[1]/div[14]/div[1]/div[1]/span[2]/div[3]/div[1]/div[1]"
        # more_stories_science_xpath = "//div[contains(text(),'More stories like this')]"
        # fewer_stories_science_xpath = "//div[contains(text(),'Fewer stories like this')]"
        # end


class HealthLocator:
    health_xpath = "//span[contains(text(),'Health')]"

    # all
    def __init__(self, i):
        self.i = i

        self.news_health_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/a[1]'
        self.save_health_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/div[1]/div[1]'
        self.share_health_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/span[1]/div[1]'
        self.more_health_xpath = f'//body/c-wiz[5]/div[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/span[{self.i}]/div[1]/div[1]/main[1]/c-wiz[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/menu[1]/span[2]/div[1]'

        # News title problem (start)
        # view_full_coverage_health_xpath = "//div[contains(text(),'Go to PolitiFact')]"
        # hide_all_health_xpath = "/html[1]/body[1]/div[14]/div[1]/div[1]/span[2]/div[3]/div[1]/div[1]"
        # more_stories_health_xpath = "//div[contains(text(),'More stories like this')]"
        # fewer_stories_health_xpath = "//div[contains(text(),'Fewer stories like this')]"
        # end


class LeftDownLocator:
    language_region_xpath = "//span[contains(text(),'Language & region')]"
    language_search_xpath = '//body/div[14]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    language_found_xpath = '/html[1]/body[1]/div[14]/div[2]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[75]/div[1]/label[1]'
    language_cancel_xpath = "//span[contains(text(),'Cancel')]"
    language_update_xpath = "//label[contains(text(),'বাংলা (বাংলাদেশ)')]"

    settings_xpath = "//span[contains(text(),'Settings')]"
    manage_xpath = '//body/c-wiz[5]/div[1]/div[2]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]'
    view_xpath = '//body/c-wiz[5]/div[1]/div[2]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[3]/div[1]/a[1]'
    theme_xpath = '//body/c-wiz[5]/div[1]/div[2]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]'
    theme_default_xpath = '//body/c-wiz[5]/div[1]/div[2]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/span[2]'
    theme_always_xpath = '//body/c-wiz[5]/div[1]/div[2]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[2]'
    theme_never_xpath = '//body/c-wiz[5]/div[1]/div[2]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[3]'

    get_android_xpath = "//span[contains(text(),'Get the Android app')]"

    get_ios_xpath = "//span[contains(text(),'Get the iOS app')]"

    feedback_xpath = "//span[contains(text(),'Send feedback')]"
    cancel_feedback_xpath = '//header/div[1]/button[1]'
    send_feedback_xpath = '//header/div[2]/label[1]/button[1]/*[1]'

    help_xpath = "//span[contains(text(),'Help')]"
