# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSignup():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_signup(self):
    self.driver.get("http://localhost:8004/")
    self.driver.set_window_size(1280, 672)
    self.driver.find_element(By.LINK_TEXT, "Admin").click()
    self.driver.find_element(By.NAME, "emailusername").click()
    self.driver.find_element(By.NAME, "emailusername").send_keys("ritik")
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("7257")
    self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
  
