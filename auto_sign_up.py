from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_drive_path = "C:\\Development\\chromedriver_win32\\chromedriver.exe"
drive = webdriver.Chrome(executable_path=chrome_drive_path)

drive.get("http://secure-retreat-92358.herokuapp.com/")

first_name = drive.find_element_by_xpath("/html/body/form/input[1]")
last_name = drive.find_element_by_xpath("/html/body/form/input[2]")
email = drive.find_element_by_xpath("/html/body/form/input[3]")

first_name.send_keys("Yang")
last_name.send_keys("Chris")
email.send_keys("kyang3200@gmail.com")

sign_up = drive.find_element_by_xpath("/html/body/form/button")
sign_up.send_keys(Keys.ENTER)


# drive.quit()