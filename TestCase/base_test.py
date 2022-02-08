from selenium import webdriver
import unittest


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = 'C:/pycharmProjects_3.9/Internship_Project/Selenium/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        print('browser open')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed')


if __name__ == '__main__':
    unittest.main()
