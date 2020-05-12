from selenium.webdriver.common.by import By

_str1 = (By.XPATH, "//div/div[2]")     # first lorem ipsum text 's element
_str2 = (By.XPATH, "//div[2]/div[2]")  # first lorem ipsum text 's element
_str3 = (By.XPATH, "//div[3]/div[2]")  # first lorem ipsum text 's element

first_avatar = "//div[@id='content']/div[1]/div/img"
second_avatar = "//div[@id='content']/div[2]/div/img"
third_avatar = "//div[@id='content']/div[3]/div/img"