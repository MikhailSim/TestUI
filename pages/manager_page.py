from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ManagerPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def go_to_manager_page(self):
        """Переход на страницу менеджера."""
        self.driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager")

    def go_to_add_customer(self):
        """Переход на страницу добавления клиента."""
        self.driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust")

    def click_customers(self):
        """Клик по кнопке 'Customers' для перехода к таблице клиентов."""
        customers_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Customers')]")))
        customers_button.click()

    def wait_for_customers_table(self):
        """Ожидание загрузки таблицы клиентов."""
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//table[@class='table table-bordered table-striped']")))

    def find_customer_by_first_name(self, first_name):
        """Поиск клиента по имени."""
        customer_rows = self.driver.find_elements(By.XPATH, "//table[@class='table table-bordered table-striped']//tbody//tr")
        return any(first_name in row.find_element(By.XPATH, ".//td[1]").text for row in customer_rows)

    def click_sort_by_first_name(self):
        """Сортировка по имени клиента."""
        first_name_header = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'First Name')]")))
        assert first_name_header.is_displayed(), "Header 'First Name' is not displayed"
        first_name_header.click()
