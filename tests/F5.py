import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tests.utils as utilfunction
from tests import ElementValue

class takeHomeIterview(unittest.TestCase):
    def setUp(self):
        print("Beginning test setup ... ")
        dir = os.getcwd()
        self.driver = webdriver.Firefox(executable_path=dir+"/geckodriver")      # Set up firefox driver (this can be modified to Chrome/IE/Safari/Headless/PhantomJS
        self.wait = WebDriverWait(self.driver, 10)                               # Set the generic wait for element = 10 second max
        self.driver.get("https://the-internet.herokuapp.com/dynamic_content?with_content=static") # Calling the URL

# Test 001
# Assert that the dynamic text (the lorem ipsum text block) on the page contains a word at least 10 characters in length.
# Stretch goal: Print the longest word on the page.
#
    def test_001(self):
        print("Running test 001 ")
        string1 = self.wait.until(EC.visibility_of_element_located(ElementValue._str1)).text  # get texts from first lorem ipsum - Text Element xpath is define in ElementValue file
        string2 = self.wait.until(EC.visibility_of_element_located(ElementValue._str2)).text  # get texts from second lorem ipsum - Text Element xpath is define in ElementValue file
        string3 = self.wait.until(EC.visibility_of_element_located(ElementValue._str3)).text  # get texts from third lorem ipsum - Text Element xpath is define in ElementValue file
        # Print out the longest words from the texts showing on the page
        print("######## Longest Words ##########")
        print(utilfunction.getlongestword(string1 + " " + string2 + " " + string3))
        print("#################################")
        # If length of the longest word larger than or equal to 10, test will pass
        assert len(utilfunction.getlongestword(string1 + " " + string2 + " " + string3)) >= 10

# Test 002
# Assert that the "Punisher" image (silhouette with a skull on his chest) does not appear on the page.
# This test may pass or fail on any given execution depending on whether the punisher happens to be on the page.
#Stretch goal: Give names to each avatar that can appear on the page and print out each avatars name.
    def test_002(self):
        print("Running test 002")
        list = []
        #Get the src of the img that being shown on the page. Then assgin to a list
        list.append(self.driver.find_element_by_xpath(ElementValue.first_avatar).get_attribute("src")) # Get first avatar's src
        list.append(self.driver.find_element_by_xpath(ElementValue.second_avatar).get_attribute("src")) # Get second avatar's src
        list.append(self.driver.find_element_by_xpath(ElementValue.third_avatar).get_attribute("src")) # Get third avatar's src
        # Print all avatar is showing on page: First check of the assignment
        utilfunction.printAvatarName(list)
        #Call checkPunisheddisplay or not function to see if Punisher was shown on the page. Passing in using a list from above's collection
        assert True == utilfunction.checkPunisherdisplay(list)

# This function is called to close the browser after each test above run
# This function can be removed if we don't want to run test independently
    def tearDown(self):
        self.driver.quit()







