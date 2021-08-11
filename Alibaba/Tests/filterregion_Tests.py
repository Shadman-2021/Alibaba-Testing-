from selenium import webdriver
import unittest
import time
from Alibaba.Pages.homePage import HomePage
from Alibaba.Pages.productPage import ProductPage

class FilterRegionTest(unittest.TestCase):
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
        filtertest.click_search_suppliers_country("Canada")
        filtertest.select_canada()
        time.sleep(2)

    def test_Product_Filter_TC_002(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)

        productsearchtest = HomePage(driver)
        productsearchtest.product_search("laptop")
        productsearchtest.click_searchbtn()

        filtertest = ProductPage(driver)
        filtertest.select_canada()
        time.sleep(2)

    def test_Product_Filter_TC_003(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)

        productsearchtest = HomePage(driver)
        productsearchtest.product_search("laptop")
        productsearchtest.click_searchbtn()

        filtertest = ProductPage(driver)
        filtertest.select_germany()
        time.sleep(2)

    def test_Product_Filter_TC_004(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)

        productsearchtest = HomePage(driver)
        productsearchtest.product_search("laptop")
        productsearchtest.click_searchbtn()

        filtertest = ProductPage(driver)
        filtertest.select_france()
        time.sleep(2)


    def test_Product_Filter_TC_005(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)

        productsearchtest = HomePage(driver)
        productsearchtest.product_search("laptop")
        productsearchtest.click_searchbtn()

        filtertest = ProductPage(driver)
        filtertest.select_netherland()
        time.sleep(2)


    def test_Product_Filter_TC_006(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)

        productsearchtest = HomePage(driver)
        productsearchtest.product_search("laptop")
        productsearchtest.click_searchbtn()

        filtertest = ProductPage(driver)
        filtertest.select_pakistan()
        time.sleep(2)

    def test_Product_Filter_TC_007(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)

        productsearchtest = HomePage(driver)
        productsearchtest.product_search("laptop")
        productsearchtest.click_searchbtn()

        filtertest = ProductPage(driver)
        filtertest.select_singapore()
        time.sleep(2)

    def test_Product_Filter_TC_008(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)

        productsearchtest = HomePage(driver)
        productsearchtest.product_search("laptop")
        productsearchtest.click_searchbtn()

        filtertest = ProductPage(driver)
        filtertest.select_thailand()
        time.sleep(2)


    def test_Product_Filter_TC_009(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)

        productsearchtest = HomePage(driver)
        productsearchtest.product_search("laptop")
        productsearchtest.click_searchbtn()

        filtertest = ProductPage(driver)
        filtertest.select_ukraine()
        time.sleep(2)


    def test_Product_Filter_TC_010(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)

        productsearchtest = HomePage(driver)
        productsearchtest.product_search("laptop")
        productsearchtest.click_searchbtn()

        filtertest = ProductPage(driver)
        filtertest.select_uk()
        time.sleep(2)

    def test_Product_Filter_TC_011(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)

        productsearchtest = HomePage(driver)
        productsearchtest.product_search("laptop")
        productsearchtest.click_searchbtn()

        filtertest = ProductPage(driver)
        filtertest.select_usa()
        time.sleep(2)

    def test_Product_Filter_TC_012(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)

        productsearchtest = HomePage(driver)
        productsearchtest.product_search("laptop")
        productsearchtest.click_searchbtn()

        filtertest = ProductPage(driver)
        filtertest.select_vietnam()
        time.sleep(2)

    def test_Product_Filter_TC_013(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)

        productsearchtest = HomePage(driver)
        productsearchtest.product_search("laptop")
        productsearchtest.click_searchbtn()

        filtertest = ProductPage(driver)
        filtertest.select_africa()
        time.sleep(2)



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Passed")


if __name__ == '__main__':
    unittest.main()
