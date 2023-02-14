from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner
import time

class GoogleSearchTest(unittest.TestCase):

    def setUp(self):
        
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://credit-auto.qsiconseil.ma/")
        input = self.driver.find_element(By.XPATH,"//*[@id='lnkAccesCreditAuto']")
        time.sleep(2)
        input.click()

    def tearDown(self):

        self.driver.quit()

    def test_ConnexionACD(self):

        username = self.driver.find_element(By.XPATH,"//*[@id='username']")
        username.send_keys("acd")
        time.sleep(3)

        password = self.driver.find_element(By.XPATH,"//*[@id='password']")
        password.send_keys("acial!acd2018")
        time.sleep(5)

        connexion =  self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[2]/div/div/form/fieldset/button")
        connexion.submit()
        time.sleep(3)

        deconnexion =  self.driver.find_element(By.XPATH, "//*[@id='lnkDeconnexion']")
        deconnexion.click()
        time.sleep(2)
    
    def test_ConnexionGCD(self):

        username = self.driver.find_element(By.XPATH,"//*[@id='username']")
        username.send_keys("gcd")
        time.sleep(3)

        password = self.driver.find_element(By.XPATH,"//*[@id='password']")
        password.send_keys("acial!gcd2018")
        time.sleep(5)

        connexion =  self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[2]/div/div/form/fieldset/button")
        connexion.submit()
        time.sleep(3)

        deconnexion =  self.driver.find_element(By.XPATH, "//*[@id='lnkDeconnexion']")
        deconnexion.click()
        time.sleep(2)

    def test_ConnexionRCD(self):

        username = self.driver.find_element(By.XPATH,"//*[@id='username']")
        username.send_keys("rcd")
        time.sleep(3)

        password = self.driver.find_element(By.XPATH,"//*[@id='password']")
        password.send_keys("acial!rcd2018")
        time.sleep(5)

        connexion =  self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[2]/div/div/form/fieldset/button")
        connexion.submit()
        time.sleep(3)

        deconnexion =  self.driver.find_element(By.XPATH, "//*[@id='lnkDeconnexion']")
        deconnexion.click()
        time.sleep(2)

    def test_ConnexionLCD(self):

        username = self.driver.find_element(By.XPATH,"//*[@id='username']")
        username.send_keys("lcd")
        time.sleep(3)

        password = self.driver.find_element(By.XPATH,"//*[@id='password']")
        password.send_keys("acial!acd2018")
        time.sleep(5)

        connexion =  self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[2]/div/div/form/fieldset/button")
        connexion.submit()
        time.sleep(3)

        deconnexion =  self.driver.find_element(By.XPATH, "//*[@id='lnkDeconnexion']") 
        deconnexion.click()
        time.sleep(2)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='rapport_script1'))