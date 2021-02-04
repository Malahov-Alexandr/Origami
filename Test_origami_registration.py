import pytest
from selenium import webdriver
import time
import precondition
import random
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get('http://malahov-b2b.devsotbit.ru/personal/?register=yes')


def Test_registration_pass():
    try:
        name = driver.find_element_by_xpath("//input[@placeholder='Например, Михаил']")
        name.send_keys(precondition.name)

        sur_name = driver.find_element_by_xpath("//input[@placeholder='Например, Иванов']")
        sur_name.send_keys(precondition.surname)

        password = driver.find_element_by_xpath("//input[@name='USER_PASSWORD']")
        password.send_keys(precondition.pas)

        conf_pas = driver.find_element_by_xpath("//input[@name='USER_CONFIRM_PASSWORD']")
        conf_pas.send_keys(precondition.confpas)

        email = driver.find_element_by_xpath("//input[@placeholder='Например, name@sotbit.ru']")
        email.send_keys('test' + str(random.randint(1,1000)) + '@mail.ru')

        btn = driver.find_element_by_xpath("//input[@name='Register']")
        btn.click()
        title = 'http://malahov-b2b.devsotbit.ru/personal/?logout=yes'


    finally:
        driver.refresh()
        driver.quit()