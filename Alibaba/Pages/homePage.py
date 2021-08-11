class HomePage:

    def __init__(self, driver):
        self.driver = driver

        #self.joinfree_button_link_text = "Join Free"
        self.myalibaba_button_xpath = "//body//div[@id='J_SC_header']//div[@data-tab='ma']//div[@data-tab='ma']//div[1]//a[1]"
        self.select_language_xpath = '//*[@id="J_SC_header"]/header/div[4]/div/div[4]/div[3]/div/div/div[1]/label'
        self.click_list_xpath = '//div[@id="J_SC_header"]//header//div//div//div//div//div//div//div//div//div[@data-role="select-language"]//div[@title="en_US"]//div'
        self.english_xpath = '//*[@id="J_SC_header"]/header/div[4]/div/div[4]/div[3]/div/div/div[2]/div[2]/div/div/div[2]/ul/li/ul/li[1]'
        self.nederland_xpath = '//*[@id="J_SC_header"]/header/div[4]/div/div[4]/div[3]/div/div/div[2]/div[2]/div/div/div[2]/ul/li/ul/li[14]'
        self.hindi_xpath = '//*[@id="J_SC_header"]/header/div[4]/div/div[4]/div[3]/div/div/div[2]/div[2]/div/div/div[2]/ul/li/ul/li[7]'
        self.deutsch_xpath = '//*[@id="J_SC_header"]/header/div[4]/div/div[4]/div[3]/div/div/div[2]/div[2]/div/div/div[2]/ul/li/ul/li[2]'
        self.portugues_xpath = '//*[@id="J_SC_header"]/header/div[4]/div/div[4]/div[3]/div/div/div[2]/div[2]/div/div/div[2]/ul/li/ul/li[2]'
        self.language_save_xpath = '//*[@id="J_SC_header"]/header/div[4]/div/div[4]/div[3]/div/div/div[2]/div[5]/button'
        self.search_textbox_name = "SearchText"
        self.search_button_xpath = '//*[@id="J_SC_header"]/header/div[2]/div[3]/div/div/form/input[4]'

   # def click_joinfree(self):
       # self.driver.find_element_by_link_text(self.joinfree_button_link_text).move_to_element().perform()

    def click_myalibaba(self):
        self.driver.find_element_by_xpath(self.myalibaba_button_xpath).click()

    def select_language(self):
        self.driver.find_element_by_xpath(self.select_language_xpath).move_to_element().perform()

    def click_language_list(self):
        self.driver.find_element_by_xpath(self.click_list_xpath).click()

    def select_english(self):
        self.driver.find_element_by_xpath(self.english_xpath).click()

    def select_nederland(self):
        self.driver.find_element_by_xpath(self.nederland_xpath).click()

    def select_hindi(self):
        self.driver.find_element_by_xpath(self.hindi_xpath).click()

    def select_deutsch(self,):
        self.driver.find_element_by_xpath(self.deutsch_xpath).click()

    def select_portugues(self):
        self.driver.find_element_by_xpath(self.portugues_xpath).click()

    def click_save(self):
        self.driver.find_element_by_xpath(self.language_save_xpath).click()

    def product_search(self, search):
        self.driver.find_element_by_name(self.search_textbox_name).clear()
        self.driver.find_element_by_name(self.search_textbox_name).send_keys(search)

    def click_searchbtn(self):
        self.driver.find_element_by_xpath(self.search_button_xpath).click()
