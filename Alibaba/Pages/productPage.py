class ProductPage:

    def __init__(self, driver):
        self.driver = driver


        self.list_products_xpath = '//div[@class="organic-gallery-offer-outter J-offer-wrapper"]'
        self.list_view_xpath = '//*[@id="root"]/div/div[4]/div[1]/div[2]/div[2]/div/a[1]'
        self.grid_view_xpath = '//*[@id="root"]/div/div[4]/div[1]/div[2]/div[2]/div/a[2]'
        self.computer_hardware_link_text = "Computer Hardware"
        self.computer_desk_link_text = "Computer Desks"
        self.tablet_pc_link_text = "Tablet PC"
        self.backpacks_link_text = "Backpacks"
        self.laptop_bag_link_text = "Laptop Bags"
        self.briefcases_link_text = "Briefcases"
        self.trade_assurance_xpath = '//*[@id="root"]/div/div[3]/div/div[2]/div[2]/a[1]/label'
        self.verified_supplier_xpath = '//*[@id="root"]/div/div[3]/div/div[2]/div[2]/a[2]/label'
        self.response_time_xpath = '//*[@id="root"]/div/div[3]/div/div[2]/div[2]/a[3]/label'
        self.paid_samples_xpath = '//*[@id="root"]/div/div[3]/div/div[3]/div[2]/a[2]/label'
        self.fast_dispatch_xpath = '//*[@id="root"]/div/div[3]/div/div[3]/div[2]/a[3]/label'
        self.duty_paid_xpath = '//*[@id="root"]/div/div[3]/div/div[3]/div[2]/a[4]/label'
        self.min_order_xpath = '//*[@id="root"]/div/div[2]/div/div[4]/div[2]/span/input'
        self.min_ok_btn_xpath = '//*[@id="root"]/div/div[3]/div/div[4]/div[2]/a/button'
        self.min_price_xpath = '//*[@id="root"]/div/div[3]/div/div[5]/div[2]/span[1]/input'
        self.max_price_xpath = '//*[@id="root"]/div/div[3]/div/div[5]/div[2]/span[3]/input'
        self.min_max_ok_btn_xpath = '//*[@id="root"]/div/div[3]/div/div[5]/div[2]/a/button'
        self.search_suppliers_country_xpath = '//*[@id="root"]/div/div[3]/div/div[6]/div[2]/div[1]/span/input'
        self.canada_xpath = "//a[@title='Canada']"
        self.germany_xpath = "//a[@title='Germany']"
        self.france_xpath = "//a[@title='France']"
        self.netherland_xpath = "//a[@title='Netherlands']"
        self.pakistan_xpath = "//a[@title='Pakistan']"
        self.singapore_xpath = "//a[@title='Singapore']"
        self.thailand_xpath = "//a[@title='Thailand']"
        self.ukraine_xpath = "//a[@title='Ukraine']"
        self.uk_xpath = "//a[@title='United Kingdom']"
        self.usa_xpath = "//a[@title='United States']"
        self.vietnam_xpath = "//a[@title='Vietnam']"
        self.africa_xpath = "//a[@title='Africa']"

    def product_count(self):
        self.driver.find_elements_by_xpath(self.list_products_xpath).length()

    def click_list_view(self):
        self.driver.find_element_by_xpath(self.list_view_xpath).click()

    def click_grid_view(self):
        self.driver.find_element_by_xpath(self.grid_view_xpath).click()

    def click_comp_hard(self):
        self.driver.find_element_by_link_text(self.computer_hardware_link_text).click()

    def click_comp_desk(self):
        self.driver.find_element_by_link_text(self.computer_desk_link_text).click()

    def click_tab_pc(self):
        self.driver.find_element_by_link_text(self.tablet_pc_link_text).click()

    def click_backpack(self):
        self.driver.find_element_by_link_text(self.backpacks_link_text).click()

    def click_lap_bag(self):
        self.driver.find_element_by_link_text(self.laptop_bag_link_text).click()

    def click_briefcase(self):
        self.driver.find_element_by_link_text(self.briefcases_link_text).click()

    def click_trade_assurance(self):
        self.driver.find_element_by_xpath(self.trade_assurance_xpath).click()

    def click_verified_supplier(self):
        self.driver.find_element_by_xpath(self.verified_supplier_xpath).click()

    def click_response_time(self):
        self.driver.find_element_by_xpath(self.response_time_xpath).click()

    def click_paid_samples(self):
        self.driver.find_element_by_xpath(self.paid_samples_xpath).click()

    def click_fast_dispatch(self):
        self.driver.find_element_by_xpath(self.fast_dispatch_xpath).click()

    def click_duty_paid(self):
        self.driver.find_element_by_xpath(self.duty_paid_xpath).click()

    def click_min_order(self, minorder):
        self.driver.find_element_by_xpath(self.min_order_xpath).click()
        self.driver.find_element_by_xpath(self.min_order_xpath).send.keys(minorder)

    def click_min_ok_btn(self):
        self.driver.find_element_by_xpath(self.min_ok_btn_xpath).click()

    def click_min_price(self, minprice):
        self.driver.find_element_by_xpath(self.min_price_xpath).clear()
        self.driver.find_element_by_xpath(self.min_price_xpath).send.keys(minprice)

    def click_max_price(self, maxprice):
        self.driver.find_element_by_xpath(self.max_price_xpath).clear()
        self.driver.find_element_by_xpath(self.max_price_xpath).send.keys(maxprice)

    def click_min_max_ok_btn(self):
        self.driver.find_element_by_xpath(self.min_max_ok_btn_xpath).click()

    def click_search_suppliers_country(self, country):
        self.driver.find_element_by_xpath(self.search_suppliers_country_xpath).clear()
        self.driver.find_element_by_xpath(self.search_suppliers_country_xpath).send.keys(country)


    def select_canada(self):
        self.driver.find_element_by_xpath(self.canada_xpath).click()

    def select_germany(self):
        self.driver.find_element_by_xpath(self.germany_xpath).click()

    def select_france(self):
        self.driver.find_element_by_xpath(self.france_xpath).click()

    def select_netherland(self):
        self.driver.find_element_by_xpath(self.netherland_xpath).click()

    def select_pakistan(self):
        self.driver.find_element_by_xpath(self.pakistan_xpath).click()

    def select_singapore(self):
        self.driver.find_element_by_xpath(self.singapore_xpath).click()

    def select_thailand(self):
        self.driver.find_element_by_xpath(self.thailand_xpath).click()

    def select_ukraine(self):
        self.driver.find_element_by_xpath(self.ukraine_xpath).click()

    def select_uk(self):
        self.driver.find_element_by_xpath(self.uk_xpath).click()

    def select_usa(self):
        self.driver.find_element_by_xpath(self.usa_xpath).click()

    def select_vietnam(self):
        self.driver.find_element_by_xpath(self.vietnam_xpath).click()

    def select_africa(self):
        self.driver.find_element_by_xpath(self.africa_xpath).click()
