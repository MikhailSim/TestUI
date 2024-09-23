import allure
from pages.manager_page import ManagerPage

@allure.feature("Сортировка клиентов")
@allure.story("Сортировка по имени")
def test_sort_customers_by_first_name(setup):
    driver = setup
    manager_page = ManagerPage(driver)

    with allure.step("Переход к таблице клиентов и ожидание загрузки"):
        manager_page.go_to_manager_page()
        manager_page.click_customers()
        manager_page.wait_for_customers_table()

    with allure.step("Клик по заголовку 'First Name' для сортировки"):
        manager_page.click_sort_by_first_name()

    with allure.step("Проверка сортировки"):
        # Проверка реализации сортировки
        pass
