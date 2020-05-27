import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tests.page_object as po
from selenium.webdriver.common.keys import Keys
import time, os
from tests import ElementLocation

class orbitz(unittest.TestCase):
    def setUp(self):
        print("Beginning test setup ... ")
        dir = os.getcwd()
        self.driver = webdriver.Firefox(executable_path=dir+"/geckodriver")      # Set up firefox driver (this can be modified to Chrome/IE/Safari/Headless/PhantomJS
        self.wait = WebDriverWait(self.driver, 10)                               # Set the generic wait for element = 10 second max
        self.driver.get("https://www.orbitz.com/") # Calling the URL

# Test 001
# Task: Search Flights to 3 cities on orbitz
#       2 adults and 2 children
# Goal: Return Total number of result

    def test_001(self):
        print("Running test 001")
        home_city = "San Jose, CA (SJC-Norman Y. Mineta San Jose Intl.)"
        second_city = "Los Angeles, CA (LAX-Los Angeles Intl.)"
        third_city = "Phoenix (PHX-All Airports)"
        po.click_by_element(self.driver, ElementLocation.css_flight_tab)  # Click on flight tab
        po.click_by_element(self.driver, ElementLocation.css_multi_city)  # Click on multi city tab
        po.click_by_element(self.driver, ElementLocation.css_add_another_flight)  # Click add another flight
        po.to_from_flight(self.driver, ElementLocation.css_first_flight_from, ElementLocation.css_first_flight_to, home_city, second_city)  # Add first flight
        po.set_date_depart(self.driver, ElementLocation.css_first_date_depart, "08/01/2020")  # Set first date departure
        po.number_of_adult(self.driver, "2")  # Set number of adults traveling
        po.number_of_children(self.driver, "2")  # Set number of children traveling
        po.set_child_age(self.driver, ElementLocation.css_first_child_age, "3")  # Set children age = 3
        po.set_child_age(self.driver, ElementLocation.css_second_child_age, "4")  # Set children age = 4
        po.to_from_flight(self.driver, ElementLocation.css_second_flight_from, ElementLocation.css_second_flight_to,
                          second_city, third_city)  # Set second flight, from LAX to Phoenix
        po.set_date_depart(self.driver, ElementLocation.css_second_date_depart, "08/02/2020")  # Set second date depart
        po.to_from_flight(self.driver, ElementLocation.css_third_flight_from, ElementLocation.css_third_flight_to,
                          third_city, home_city)  # Set third flight, from Phoenix to SJC
        po.set_date_depart(self.driver, ElementLocation.css_third_date_depart, "08/11/2020")  # Set third date depart
        po.click_by_element(self.driver, ElementLocation.css_search_button)  # Click on Search Button
        all_result = po.get_flight_result(self.driver)  # Get all result from result panel
        print("+++++++++ TOTAL FLIGHT RESULT AVAILABLE ++++++++++")
        print(po.get_total_result(all_result))  # Print only result line
        print("++++++++++++++++++++++++++++++++++++++++++++++++++")

        # Decide with option is lowest price and short route
        # Select FLight 1
        self.driver.find_element_by_css_selector(ElementLocation.css_sort_by).__setattr__("price:asc", "value")
        po.click_by_element(self.driver, ElementLocation.css_no_change_fee_radio)
        po.click_by_element(self.driver, ElementLocation.css_nonstop_radio)
        time.sleep(5)
        print("+++++++++ TOP PRICE VALUE +++++++++")
        print(po.get_text_from_xpath(self.driver, ElementLocation.xpath_top_price_value))
        print("+++++++++++++++++++++++++++++++++++")
        po.click_by_element_xpath(self.driver, ElementLocation.xpath_result_button)
        po.click_by_element_xpath(self.driver, ElementLocation.xpath_select_this_fare)
        # Select Flight 2
        time.sleep(3)
        self.driver.find_element_by_css_selector(ElementLocation.css_sort_by).__setattr__("price:asc", "value")
        po.click_by_element(self.driver, ElementLocation.css_no_change_fee_radio)
        po.click_by_element(self.driver, ElementLocation.css_nonstop_radio)
        time.sleep(5)
        po.click_by_element_xpath(self.driver, ElementLocation.xpath_result_button)
        po.click_by_element_xpath(self.driver, ElementLocation.xpath_select_this_fare)
        # Select Flight 3
        time.sleep(3)
        self.driver.find_element_by_css_selector(ElementLocation.css_sort_by).__setattr__("price:asc", "value")
        po.click_by_element(self.driver, ElementLocation.css_no_change_fee_radio)
        time.sleep(5)
        po.click_by_element_xpath(self.driver, ElementLocation.xpath_result_button)
        po.click_by_element_xpath(self.driver, ElementLocation.xpath_select_this_fare)

        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ElementLocation.css_result_flight1)))
        print("+++++++++ Validate Correct Flight Chosen +++++++++")
        str1 = po.get_flight_result_by_css(self.driver, ElementLocation.css_result_flight1)
        str2 = po.get_flight_result_by_css(self.driver, ElementLocation.css_result_flight2)
        str3 = po.get_flight_result_by_xpath(self.driver, ElementLocation.xpath_result_flight3)
        str4 = po.get_flight_result_by_xpath(self.driver, ElementLocation.xpath_result_flight4)
        str5 = po.get_flight_result_by_xpath(self.driver, ElementLocation.xpath_result_flight5)
        str6 = po.get_flight_result_by_xpath(self.driver, ElementLocation.xpath_result_flight6)
        print("FROM : " + str1)
        print("TO : " + str2)
        print("FROM : " + str3)
        print("TO : " + str4)
        print("FROM : " + str5)
        print("TO : " + str6)
        assert "San Jose (SJC)" == str1
        assert "Los Angeles (LAX)" == str2
        assert "Los Angeles (LAX)" == str3
        assert "Phoenix (PHX)" == str4
        assert "Phoenix (PHX)" == str5
        assert "San Jose (SJC)" == str6

    def tearDown(self):
        self.driver.quit()









