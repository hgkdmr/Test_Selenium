# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestBlankpasswordlogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()

  def test_blankpasswordlogin(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.set_window_size(1536, 816)
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        body_element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(body_element).perform()
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Username is required"












""" 
    def test_blankpasswordlogin(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1536, 816)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Username is required" """