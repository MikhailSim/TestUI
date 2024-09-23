import allure
from pages.manager_page import ManagerPage
from pages.customer_page import CustomerPage

@allure.feature("Добавление клиентов")
@allure.story("Добавление нового клиента")
def test_add_customer(setup):
    driver = setup
    manager_page = ManagerPage(driver)
    customer_page = CustomerPage(driver)

    with allure.step("Переход на страницу добавления клиента"):
        manager_page.go_to_add_customer()

    with allure.step("Заполнение формы добавления клиента"):
        first_name = "John"
        last_name = "Doe"
        post_code = "12345"

        customer_page.enter_first_name(first_name)
        customer_page.enter_last_name(last_name)
        customer_page.enter_post_code(post_code)

    with allure.step("Нажатие на кнопку 'Add Customer'"):
        customer_page.click_add_customer()

    with allure.step("Подтверждение добавления клиента"):
        alert_text = customer_page.confirm_alert()
        assert "Customer added successfully" in alert_text, "Сообщение об успешном добавлении клиента не отображается"

    with allure.step("Проверка, что клиент был добавлен"):
        manager_page.go_to_manager_page()
        manager_page.click_customers()
        manager_page.wait_for_customers_table()

        # Проверка по имени клиента
        assert manager_page.find_customer_by_first_name(first_name), f"Клиент с именем {first_name} не найден в таблице"
