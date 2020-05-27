import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tests.page_object as utilfunction
from selenium.webdriver.common.keys import Keys
import time, os
from tests import ElementLocation


def to_from_flight(driver, element_from, element_to, str1, str2):
    # Set first City departing from SJC
    from_city_1 = driver.find_element_by_css_selector(element_from)
    from_city_1.send_keys(str1)
    # Set first City arriving LAX
    to_city_1 = driver.find_element_by_css_selector(element_to)
    to_city_1.send_keys(str2)


def set_date_depart(driver, element_date, date_string):
    input_date1 = driver.find_element_by_css_selector(element_date)
    input_date1.send_keys(date_string)


def number_of_adult(driver, number_of_adult):
    input_num_adult = driver.find_element_by_css_selector(ElementLocation.css_num_of_adult)
    input_num_adult.send_keys(number_of_adult)


def number_of_children(driver, number_of_children):
    input_num_child = driver.find_element_by_css_selector(ElementLocation.css_num_of_child)
    input_num_child.send_keys(number_of_children)


def set_child_age(driver, element_child_age, age):
    input_child_age_1 = driver.find_element_by_css_selector(element_child_age)
    input_child_age_1.send_keys(age)


def click_by_element(driver, element_to_click):
    driver.find_element_by_css_selector(element_to_click).click()


def click_by_element_xpath(driver, element_to_click):
    driver.find_element_by_xpath(element_to_click).click()


def get_text_from_xpath(driver, element_xpath_price_locaton):
    price = driver.find_element_by_xpath(element_xpath_price_locaton).text
    return price

def get_flight_result_by_css(driver, location):
    str1 = driver.find_element_by_css_selector(location).text
    return str1


def get_flight_result_by_xpath(driver, location):
    str1 = driver.find_element_by_xpath(location).text
    return str1


# this method is to return the number of results
def get_total_result(str1):
    list1 = str1.splitlines()
    result = len(list1) - 1
    return_result = (list1[result])
    return return_result


def get_flight_result(driver):
    all_result = ''
    count = 0
    while not all_result:
        count = count + 1
        if count < 10:
            all_result = driver.find_element_by_css_selector('#flightModuleList').text
            print("WAITING FOR RESULT PANEL......")
            time.sleep(2)
    return all_result
