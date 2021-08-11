from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time
from Alibaba.Pages.homePage import HomePage

class LanguageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def Change_language_TC_001(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        a = ActionChains(driver)
        changelanguageTest = HomePage(driver)
        time.sleep(5)
        changelanguageTest.select_language()
        changelanguageTest.click_language_list()
        changelanguageTest.select_nederland()
        changelanguageTest.click_save()



    def Change_language_TC_002(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        a = ActionChains(driver)
        changelanguageTest = HomePage(driver)
        time.sleep(5)
        changelanguageTest.select_language()
        changelanguageTest.click_language_list()
        changelanguageTest.select_nederland()
        changelanguageTest.click_save()
        time.sleep(2)
        changelanguageTest.select_english()
        changelanguageTest.click_save()

    def Change_language_TC_003(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        a = ActionChains(driver)
        changelanguageTest = HomePage(driver)
        time.sleep(5)
        changelanguageTest.select_language()
        changelanguageTest.click_language_list()
        changelanguageTest.select_hindi()
        changelanguageTest.click_save()

    def Change_language_TC_004(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        a = ActionChains(driver)
        changelanguageTest = HomePage(driver)
        time.sleep(5)
        changelanguageTest.select_language()
        changelanguageTest.click_language_list()
        changelanguageTest.select_deutsch()
        changelanguageTest.click_save()

    def Change_language_TC_005(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        a = ActionChains(driver)
        changelanguageTest = HomePage(driver)
        time.sleep(5)
        changelanguageTest.select_language()
        changelanguageTest.click_language_list()
        changelanguageTest.select_portugues()
        changelanguageTest.click_save()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Passed")

    if __name__ == '__main__':
        unittest.main()
