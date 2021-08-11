from selenium import webdriver
import unittest
import time
from Alibaba.Pages.homePage import HomePage
from Alibaba.Pages.productPage import ProductPage

class FilterMinOrderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        pass

    def test_Product_Filter_TC_001(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)

        productsearchtest = HomePage(driver)
        productsearchtest.product_search("laptop")
        productsearchtest.click_searchbtn()

        filtertest = ProductPage(driver)
        filtertest.click_min_order("100")
        filtertest.click_min_ok_btn()
        time.sleep(2)



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Passed")


if __name__ == '__main__':
    unittest.main()
