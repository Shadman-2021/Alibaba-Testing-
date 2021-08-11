from selenium import webdriver
import unittest
import time
from Alibaba.Pages.homePage import HomePage
from Alibaba.Pages.productPage import ProductPage

class ProductCategoryTest(unittest.TestCase):
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
        filtertest.click_comp_hard()
        time.sleep(2)

    def test_Product_Filter_TC_002(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)

        productsearchtest = HomePage(driver)
        productsearchtest.product_search("laptop")
        productsearchtest.click_searchbtn()

        filtertest = ProductPage(driver)
        filtertest.click_comp_hard()
        time.sleep(2)

    def test_Product_Filter_TC_003(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)

        productsearchtest = HomePage(driver)
        productsearchtest.product_search("laptop")
        productsearchtest.click_searchbtn()

        filtertest = ProductPage(driver)
        filtertest.click_comp_desk()
        time.sleep(2)

    def test_Product_Filter_TC_004(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)


        productsearchtest = HomePage(driver)
        productsearchtest.product_search("laptop")
        productsearchtest.click_searchbtn()

        filtertest = ProductPage(driver)
        filtertest.click_tab_pc()
        time.sleep(2)

    def test_Product_Filter_TC_005(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)


        productsearchtest = HomePage(driver)
        productsearchtest.product_search("laptop")
        productsearchtest.click_searchbtn()

        filtertest = ProductPage(driver)
        filtertest.click_backpack()
        time.sleep(2)


    def test_Product_Filter_TC_006(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)


        productsearchtest = HomePage(driver)
        productsearchtest.product_search("laptop")
        productsearchtest.click_searchbtn()

        filtertest = ProductPage(driver)
        filtertest.click_lap_bag()
        time.sleep(2)

    def test_Product_Filter_TC_007(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)


        productsearchtest = HomePage(driver)
        productsearchtest.product_search("laptop")
        productsearchtest.click_searchbtn()

        filtertest = ProductPage(driver)
        filtertest.click_briefcase()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Passed")


if __name__ == '__main__':
    unittest.main()