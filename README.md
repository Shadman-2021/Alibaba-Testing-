Selenium Page Object Model with Python on Alibaba
Page-object-model (POM) is a pattern that you can apply it to develop efficient automation framework. With page-model, it is possible to minimise maintenance cost. Basically page-object means that your every page is inherited from a base class which includes basic functionalities for every pages. If you have some new functionality that every pages have, you can simple add it to the base class.

HomePage class include basic functionality and driver initialization

homePage.py
class HomePage(object):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        pass

  
signinPage and productPage is derived from the `HomePage class, it contains methods related to this page, which will be used to create test steps.


When you want to write tests, you should derive your test class from UnitTest which holds basic functionality for your tests. Then you can call page and related methods in accordance with the steps in the test cases

class SigninTest(unittest.TestCase):

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

[Test Case (Alibaba web)_14.06.2021.xlsx](https://github.com/Shadman-2021/Assignment1/files/6968018/Test.Case.Alibaba.web._14.06.2021.xlsx)
If you want to run all tests, you should type:
If you want to run just a class, you should type:

python -m unittest 

If you want to run just a class, you should type:


python -m unittest tests.signin_tests.signinPage


If you want to run just a test method, you should type:


python -m unittest tests.signin_tests.signinPage.test_Signin_TC_001
