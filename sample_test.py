from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select




print("Browser Invoked")
driver = webdriver.Firefox(executable_path='/Users/jilvelasquez/Development/pycharm/orangehrm-bdd/drivers/geckodriver')
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)
driver.maximize_window()
action = ActionChains(driver)

# Login
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.find_element_by_id('txtUsername').send_keys('Admin')
driver.find_element_by_id('txtPassword').send_keys('admin123')
driver.find_element_by_id('btnLogin').click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#welcome")))



driver.find_element_by_id("btnAdd").click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "systemUser")))

Select(driver.find_element_by_id("systemUser_userType")).select_by_visible_text("Admin")

driver.find_element_by_id("systemUser_employeeName_empName").send_keys("Hannah Flores")
driver.find_element_by_id("systemUser_userName").send_keys("Sample")
Select(driver.find_element_by_id("systemUser_status")).select_by_visible_text("Disabled")
driver.find_element_by_id("systemUser_password").send_keys("Sample1234")
driver.find_element_by_id("systemUser_confirmPassword").send_keys("Sample1234")
