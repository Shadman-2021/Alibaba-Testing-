from selenium import webdriver
import unittest
import time
from Alibaba.Pages.homePage import HomePage
from Alibaba.Pages.productPage import ProductPage


class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def Search_product_TC_001(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        searchTest = HomePage(driver)
        time.sleep(2)
        searchTest.click_searchbtn()

    def Search_product_TC_002(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        searchTest = HomePage(driver)
        time.sleep(5)
        searchTest.product_search("laptop")
        searchTest.click_searchbtn()

    def Search_product_TC_003(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        searchTest = HomePage(driver)
        time.sleep(5)
        searchTest.product_search("samsung mobile phone")
        searchTest.click_searchbtn()

    def Search_product_TC_004(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        searchTest = HomePage(driver)
        time.sleep(5)
        searchTest.product_search("samsung")
        searchTest.click_searchbtn()
        List_products = ProductPage(driver)
        print("Count of Products on first page is:" + List_products.product_count())

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Passed")


if __name__ == '__main__':
    unittest.main()