from selenium import webdriver
import unittest
import time
from Alibaba.Pages.homePage import HomePage
from Alibaba.Pages.signinPage import SigninPage


class SigninTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        pass

    def test_Signin_TC_001(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)

        signinPreTest = HomePage(driver)
        #signinPreTest.click_joinfree()
        # 1. click on My alibaba button
        signinPreTest.click_myalibaba()
        signinTest = SigninPage(driver)
        # 2. keep empty account field
        # 3. keep empty password field
        # 4. click on "sign in" Button
        signinTest.click_signin()
        time.sleep(2)

    # 1. click on My alibaba button
    # 2. Type email on account field
    # 3. keep empty password field
    # 4. click on "sign in" Button

    def test_Signin_TC_002(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)

        signinPreTest = HomePage(driver)
       # signinPreTest.click_joinfree()
        # 1. click on My alibaba button
        signinPreTest.click_myalibaba()
        signinTest = SigninPage(driver)
        # 2. Enter email id on  account field
        signinTest.enter_username("praveen@gmail.com")
        # 3. keep empty password field
        # 4. click on "sign in" Button
        signinTest.click_signin()
        time.sleep(2)

    def test_Signin_TC_003(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)

        signinPreTest = HomePage(driver)
        #signinPreTest.click_joinfree()
        # 1. click on My alibaba button
        signinPreTest.click_myalibaba()
        signinTest = SigninPage(driver)
        # 2. Enter email id on  account field
        signinTest.enter_username("praveen@gmail.com")
        # 3. Enter wrong password in password field
        signinTest.enter_password("alibab12345")
        # 4. click on "sign in" Button
        signinTest.click_signin()
        time.sleep(2)

    def test_Signin_TC_004(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)

        signinPreTest = HomePage(driver)
        #signinPreTest.click_joinfree()
        # 1. click on My alibaba button
        signinPreTest.click_myalibaba()
        signinTest = SigninPage(driver)
        # 2. Keep  email id field empty
        signinTest.enter_username(" ")
        # 3. Enter right password in password field
        signinTest.enter_password("QWEASDzxc1231234")
        # 4. click on "sign in" Button
        signinTest.click_signin()
        time.sleep(2)

    def test_Signin_TC_005(self):
        driver = self.driver
        driver.get("https://www.alibaba.com/")
        time.sleep(2)

        signinPreTest = HomePage(driver)
        #signinPreTest.click_joinfree()
        # 1. click on My alibaba button
        signinPreTest.click_myalibaba()
        signinTest = SigninPage(driver)
        # 2. Keep  email id field empty
        signinTest.enter_username("shadman_ahsan@yahoo.com")
        # 3. Enter right password in password field
        signinTest.enter_password("QWEASDzxc1231234")
        # 4. click on "sign in" Button
        signinTest.click_signin()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Passed")


if __name__ == '__main__':
    unittest.main()
