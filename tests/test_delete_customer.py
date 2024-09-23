import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.manager_page import ManagerPage
from pages.customer_page import CustomerPage

@allure.feature("Удаление клиента")
@allure.story("Удаление клиента по длине имени")
def test_delete_customer_by_name_length(setup):
    driver = setup
    manager_page = ManagerPage(driver)
    customer_page = CustomerPage(driver)

    with allure.step("Переход на страницу клиентов"):
        manager_page.click_customers()

    with allure.step("Ожидание таблицы клиентов"):
        manager_page.wait_for_customers_table()

    with allure.step("Получение списка клиентов и вычисление средней длины имени"):
        customer_rows = driver.find_elements(By.XPATH, "//table[@class='table table-bordered table-striped']//tbody//tr")
        name_lengths = [len(row.find_element(By.XPATH, ".//td[1]").text) for row in customer_rows]
        average_length = sum(name_lengths) / len(name_lengths)

    with allure.step("Удаление клиента с длиной имени, близкой к средней"):
        closest_customer = min(customer_rows, key=lambda row: abs(len(row.find_element(By.XPATH, ".//td[1]").text) - average_length))
        closest_customer_name = closest_customer.find_element(By.XPATH, ".//td[1]").text
        closest_customer.find_element(By.XPATH, ".//button[contains(text(), 'Delete')]").click()

    with allure.step("Проверка, что клиент был удален"):
        manager_page.wait_for_customers_table()
        assert not manager_page.find_customer_by_first_name(closest_customer_name), f"Клиент с именем {closest_customer_name} не был удален"
