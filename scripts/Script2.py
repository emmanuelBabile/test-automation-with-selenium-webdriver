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

    def test_UC1(self):

        username = self.driver.find_element(By.XPATH,"//*[@id='username']")
        username.send_keys("gcd")
        time.sleep(3)

        password = self.driver.find_element(By.XPATH,"//*[@id='password']")
        password.send_keys("acial!gcd2018")
        time.sleep(5)

        connexion =  self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[2]/div/div/form/fieldset/button")
        connexion.submit()
        time.sleep(3)

        simulation =  self.driver.find_element(By.XPATH, "//*[@id='lnkSimulation']")
        simulation.click()
        time.sleep(1)

        montantAchat = self.driver.find_element(By.XPATH,"//*[@id='form_simulation_montantAchat']")
        montantAchat.send_keys("5500")
        time.sleep(3)

        montantCredit = self.driver.find_element(By.XPATH,"//*[@id='form_simulation_montantCredit']")
        montantCredit.send_keys("5000")
        time.sleep(3)

        duree = self.driver.find_element(By.XPATH,"//*[@id='form_simulation_duree']")
        duree.send_keys("18")
        time.sleep(3)

        dropdownCategorie = self.driver.find_element(By.XPATH,"//*[@id='form_simulation_categorie']")
        dropdownCategorie.click()
        time.sleep(2)
        choixCategorieB = self.driver.find_element(By.XPATH,"//*[@id='form_simulation_categorie']/option[2]")
        choixCategorieB.click()
        time.sleep(3)
        
        calcul = self.driver.find_element(By.XPATH, "//*[@id='calcul']")
        calcul.submit()
        time.sleep(3)

        echeancier = self.driver.find_element(By.XPATH,"//*[@id='ech']")
        echeancier.click()
        time.sleep(4)

        creerContrat = self.driver.find_element(By.XPATH,"/html/body/div[2]/form/fieldset/div[1]/a[2]")
        creerContrat.click()
        time.sleep(2)

        customerName = self.driver.find_element(By.XPATH,"//*[@id='name']")
        customerName.send_keys("DUCLOS")
        time.sleep(2)

        customerFirstName = self.driver.find_element(By.XPATH,"//*[@id='firstname']")
        customerFirstName.send_keys("Jean")
        time.sleep(2)

        recherche =  self.driver.find_element(By.XPATH, "/html/body/div[2]/fieldset/form/div/input[3]")
        recherche.submit()
        time.sleep(4)
        
        checkCustomer = self.driver.find_element(By.XPATH, "/html/body/div[2]/fieldset/form[2]/table/tbody/tr[1]/td[1]/div/input")
        self.driver.execute_script("arguments[0].click();", checkCustomer)
        time.sleep(2)

        validateCustomer =  self.driver.find_element(By.XPATH, "/html/body/div[2]/fieldset/form[2]/button")
        validateCustomer.click()
        time.sleep(3)
        
        printContract = self.driver.find_element(By.XPATH,"/html/body/div[2]/fieldset/div/button[1]")
        printContract.click()
        time.sleep(5)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='rapport_script2'))