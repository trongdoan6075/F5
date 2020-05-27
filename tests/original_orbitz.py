import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tests.page_object as utilfunction
from selenium.webdriver.common.keys import Keys
import time, os
from tests import ElementLocation

class takeHomeIterview(unittest.TestCase):
    def setUp(self):
        print("Beginning test setup ... ")
        dir = os.getcwd()
        self.driver = webdriver.Firefox(executable_path=dir+"/geckodriver")      # Set up firefox driver (this can be modified to Chrome/IE/Safari/Headless/PhantomJS
        self.wait = WebDriverWait(self.driver, 10)                               # Set the generic wait for element = 10 second max
        self.driver.get("https://www.orbitz.com/") # Calling the URL

# Test 001
# Assert that the dynamic text (the lorem ipsum text block) on the page contains a word at least 10 characters in length.
# Stretch goal: Print the longest word on the page.
#
    def test_001(self):
        print("Running test 001")
        self.driver.find_element_by_css_selector(ElementLocation.css_flight_tab).click()
        self.driver.find_element_by_css_selector(ElementLocation.css_multi_city).click()
        # Click add another flight
        self.driver.find_element_by_css_selector('#add-flight-leg-hp-flight').click()
        # Set first City departing from SJC
        from_city_1 = self.driver.find_element_by_css_selector(ElementLocation.css_first_flight_from)
        from_city_1.send_keys("San Jose, CA (SJC-Norman Y. Mineta San Jose Intl.)")
        # Set first City arriving LAX
        to_city_1 = self.driver.find_element_by_css_selector(ElementLocation.css_first_flight_to)
        to_city_1.send_keys("Los Angeles, CA (LAX-Los Angeles Intl.)")
        # Set Date
        input_date1 = self.driver.find_element_by_css_selector(ElementLocation.css_first_date_depart)
        input_date1.send_keys("08/01/2020")
        # Set number of adults traveling
        input_num_adult = self.driver.find_element_by_css_selector(ElementLocation.css_num_of_adult)
        input_num_adult.send_keys("2")
        # Set number of children traveling
        input_num_child = self.driver.find_element_by_css_selector(ElementLocation.css_num_of_child)
        input_num_child.send_keys("2")
        # Set children age
        input_child_age_1 = self.driver.find_element_by_css_selector(ElementLocation.css_first_child_age)
        input_child_age_1.send_keys("3")
        input_child_age_2 = self.driver.find_element_by_css_selector(ElementLocation.css_second_child_age)
        input_child_age_2.send_keys("4")

        # Set second flight, from LAX to Phoenix
        from_city_2 = self.driver.find_element_by_css_selector(ElementLocation.css_second_flight_from)
        from_city_2.send_keys("Los Angeles, CA (LAX-Los Angeles Intl.)")
        to_city_2 = self.driver.find_element_by_css_selector(ElementLocation.css_second_flight_to)
        to_city_2.send_keys("Phoenix (PHX-All Airports)")
        # Set second date depart
        second_date_depart = self.driver.find_element_by_css_selector(ElementLocation.css_second_date_depart)
        second_date_depart.send_keys("08/02/2020")
        #webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        #time.sleep(10)

        # Set third flight, from Phoenix to SJC
        from_city_3 = self.driver.find_element_by_css_selector(ElementLocation.css_third_flight_from)
        from_city_3.send_keys("Phoenix (PHX-All Airports)")
        to_city_3 = self.driver.find_element_by_css_selector(ElementLocation.css_third_flight_to)
        to_city_3.send_keys("San Jose, CA (SJC-Norman Y. Mineta San Jose Intl.)")
        # Set third date depart
        third_date_depart = self.driver.find_element_by_css_selector(ElementLocation.css_third_date_depart)
        third_date_depart.send_keys("08/11/2020")
        # Click on Search Button
        self.driver.find_element_by_css_selector(ElementLocation.css_search_button).click()
        time.sleep(10)
        all_result = ''
        while not all_result:
            all_result = self.driver.find_element_by_css_selector('#flightModuleList').text
            time.sleep(2)
        print(all_result)
        print("+++++++++ RESULT AVAILABLE ++++++++++")
        print(utilfunction.get_total_result(all_result))





# This function is called to close the browser after each test above run
# This function can be removed if we don't want to run test independently
    def tearDown(self):
        self.driver.quit()







