from selenium.webdriver.common.by import By

class CustomerPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first_name):
        first_name_input = self.driver.find_element(By.XPATH, "//input[@ng-model='fName']")
        first_name_input.send_keys(first_name)

    def enter_last_name(self, last_name):
        last_name_input = self.driver.find_element(By.XPATH, "//input[@ng-model='lName']")
        last_name_input.send_keys(last_name)

    def enter_post_code(self, post_code):
        post_code_input = self.driver.find_element(By.XPATH, "//input[@ng-model='postCd']")
        post_code_input.send_keys(post_code)

    def click_add_customer(self):
        add_customer_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        add_customer_button.click()

    def confirm_alert(self):
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text
