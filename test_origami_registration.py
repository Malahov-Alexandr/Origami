import precondition
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

@pytest.fixture(scope="class")
def driver():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class Testregistration():
    def test_add_item_to_card(self, driver):
        driver.get(precondition.main_link)
        driver.maximize_window()
        driver.find_element_by_xpath(
            "//div[@class='check_basket_213 product_card__block_item_inner-wrapper']//div[@class='product_card__block_item_inner']//div[@class='product_card__inner ']//div[@class='product_card__inner-wrapper']//form[@class='product-card-inner__form']//div[@class='product-card-inner__buttons-block']//div[@class='product-card-inner__buy']//div//button[@type='button'][contains(text(),'В корзину')]").click()
        in_card = driver.find_element_by_xpath(
            "//div[@class='check_basket_213 product_card__block_item_inner-wrapper']//a[@class='product-card-inner__product-basket-btn'][contains(text(),'В корзине')]")
        time.sleep(1)
        assert in_card.text == 'В корзине'



    def test_reg_pas(self,driver):
        driver.get(precondition.reg_link)
        driver.maximize_window()
        login = driver.find_element_by_id("USER_LOGIN")
        login.send_keys(precondition.Login())
        pasw = driver.find_element_by_id("USER_PASSWORD")
        pasw.send_keys("123123")
        pasw_conf = driver.find_element_by_id("USER_CONFIRM_PASSWORD")
        pasw_conf.send_keys("123123")

        email = driver.find_element_by_id("USER_EMAIL")
        email.send_keys(precondition.Mail())

        button = driver.find_element_by_xpath("//input[@name='Register']")
        driver.execute_script("arguments[0].click();", button)
        title = driver.title
        assert title == 'Личный кабинет'


