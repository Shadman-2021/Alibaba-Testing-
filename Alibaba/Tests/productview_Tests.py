from selenium import webdriver
import unittest
import time
from Alibaba.Pages.homePage import HomePage
from Alibaba.Pages.productPage import ProductPage



class ProductviewTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        pass

    def test_Product_View_TC_001(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)


        productviewtest = HomePage(driver)
        productviewtest.product_search("laptop")
        productviewtest.click_searchbtn()
        viewtest = ProductPage(driver)
        viewtest.click_list_view()
        time.sleep(2)

    def test_Product_View_TC_002(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)

        productviewtest = HomePage(driver)
        productviewtest.product_search("laptop")
        productviewtest.click_searchbtn()
        viewtest = ProductPage(driver)
        viewtest.click_grid_view()
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Passed")


if __name__ == '__main__':
    unittest.main()