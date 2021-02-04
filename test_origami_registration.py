import precondition
import pytest
from selenium import webdriver
link = 'http://origami-sasha.devsotbit.ru/personal/?register=yes'


@pytest.fixture(scope="class")
def driver():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")



class TestRegistration():
    def test_empty_fields(self,driver):
        driver.get(link)
        driver.maximize_window()
        driver.find_element_by_name('Register').click()
        notify = driver.find_element_by_xpath("//div[@class='origami-auth__result']//p")
        assert len(notify.text) == 99



    def test_wrong_pasw(self,driver):
        driver.get(link)
        driver.maximize_window()
        login = driver.find_element_by_id("USER_LOGIN")
        login.send_keys(precondition.Login())
        pasw = driver.find_element_by_id("USER_PASSWORD")
        pasw.send_keys("123123")
        pasw_conf = driver.find_element_by_id("USER_CONFIRM_PASSWORD")
        pasw_conf.send_keys("123")

        email = driver.find_element_by_id("USER_EMAIL")
        email.send_keys(precondition.Mail())

        button = driver.find_element_by_xpath("//input[@name='Register']")
        driver.execute_script("arguments[0].click();", button)
        notify_site = driver.find_element_by_xpath("//font[@class='errortext']")
        text_example = 'Неверное подтверждение пароля.'
        assert notify_site.text == text_example, 'Неверное уведомление'


    def test_no_conf_pasw(self,driver):
        driver.get(link)
        driver.maximize_window()
        login = driver.find_element_by_id("USER_LOGIN")
        login.send_keys(precondition.Login())
        pasw = driver.find_element_by_id("USER_PASSWORD")
        pasw.send_keys("123123")

        email = driver.find_element_by_id("USER_EMAIL")
        email.send_keys(precondition.Mail())

        button = driver.find_element_by_xpath("//input[@name='Register']")
        driver.execute_script("arguments[0].click();", button)
        notify_site = driver.find_element_by_xpath("//font[@class='errortext']")
        text_example = 'Неверное подтверждение пароля.'
        assert notify_site.text == text_example, 'Неверное уведомление'