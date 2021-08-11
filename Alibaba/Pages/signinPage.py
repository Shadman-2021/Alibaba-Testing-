class SigninPage:

    def __init__(self, driver):
        self.driver = driver


        self.username_textbox_id = "fm-login-id"
        self.password_textbox_id = "fm-login-password"
        self.signin_button_id = "fm-login-submit"



    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_signin(self):
        self.driver.find_element_by_id(self.signin_button_id).click()
