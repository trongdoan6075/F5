import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class takeHomeIterview(unittest.TestCase):
    def setUp(self):
        print("Beginning test setup ... ")
        dir = os.getcwd()
        self.driver = webdriver.Firefox(executable_path=dir+"/geckodriver")      # Set up firefox driver (this can be modified to Chrome/IE/Safari/Headless/PhantomJS
        self.wait = WebDriverWait(self.driver, 15)                               # Set the generic wait for element = 10 second max
        self.driver.get("https://the-internet.herokuapp.com/dynamic_content?with_content=static") # Calling the URL

# Test 001
# Assert that the dynamic text (the lorem ipsum text block) on the page contains a word at least 10 characters in length.
# Stretch goal: Print the longest word on the page.
#
#Return: consequuntur, necessitatibus, exercitationem
    def test_001(self):
        print("Running test 001 ")
        _str1 = (By.XPATH, "//div/div[2]")    # first lorem ipsum text 's element
        _str2 = (By.XPATH, "//div[2]/div[2]") # first lorem ipsum text 's element
        _str3 = (By.XPATH, "//div[3]/div[2]") # first lorem ipsum text 's element
        string1 = self.wait.until(EC.visibility_of_element_located(_str1)).text  # get texts from first lorem ipsum
        string2 = self.wait.until(EC.visibility_of_element_located(_str2)).text  # get texts from second lorem ipsum
        string3 = self.wait.until(EC.visibility_of_element_located(_str3)).text  # get texts from third lorem ipsum
        print(getlongestword(string1 + " " + string2 + " " + string3))           # Print out all the texts being show on screen: First check of the assigment
        assert str(getlongestword(string1 + " " + string2 + " " + string3)) in "consequuntur, necessitatibus, exercitationem" # Calling the method to get longest word from string: second check of the assignment

# Assert that the "Punisher" image (silhouette with a skull on his chest) does not appear on the page.
# This test may pass or fail on any given execution depending on whether the punisher happens to be on the page.
#Stretch goal: Give names to each avatar that can appear on the page and print out each avatars name.
    def test_002(self):
        print("Running test 002")
        list = []
        #Get the src of the img that being shown on the page. Then assgin to a list
        list.append(self.driver.find_element_by_xpath("//div[@id='content']/div[1]/div/img").get_attribute("src")) # Get first avatar's src
        list.append(self.driver.find_element_by_xpath("//div[@id='content']/div[2]/div/img").get_attribute("src")) # Get second avatar's src
        list.append(self.driver.find_element_by_xpath("//div[@id='content']/div[3]/div/img").get_attribute("src")) # Get third avatar's src
        # Print all avatar is showing on page: First check of the assignment
        printAvatarName(list)
        #Call checkPunisheddisplay or not function to see if Punisher was shown on the page. Passing in using a list from above's collection
        assert True == checkPunisherdisplay(list)

# This function is called to close the browser after each run
    def tearDown(self):
        self.driver.quit()

# This method is to get the longest length of the word from the list.
def getlongestword(str):
    temp = 0
    string = ''
    list = str.split(" ")
    for word in list:
        if len(word) > temp:
            temp = len(word)
            string = word
    return string

# This method is to print the name of the avatar that is showing on the page.
# Base on the mapping hash created, name will be printed accordingly
def printAvatarName(list):
    hash = {"https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-1.jpg": "Mario",
            "https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-2.jpg": "Robot",
            "https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-3.jpg": "Punisher",
            "https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-5.jpg": "BATMAN",
            "https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-6.jpg": "Star War",
            "https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-7.jpg": "Circus Man"}
    counter = 1
    for i in range(0, len(list)):
        for k, v in hash.items():
            if list[i] == k:
                print(str(counter) + ". " + "Avatar's Name: " + v)
                counter += 1

# This method is to check if the Punisher is shown on the page or not.
# return True if it shows, otherwise return False
def checkPunisherdisplay(list):
    target_silhouette = "https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-3.jpg"

    for i in range(0, len(list)):
        if list[i] == target_silhouette:
            return True
    return False


