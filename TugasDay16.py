import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

class TestLogin(unittest.TestCase):
    
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--incognito")  # Menambahkan opsi untuk membuka Chrome dalam mode incognito
        driver_service = Service(executable_path="C:/webdrivers/chromedriver")
        self.browser = webdriver.Chrome(service=driver_service, options=chrome_options)

    
    def test_a_success_login(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        
        # Isi username dan password
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin") # isi username
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123") # isi password
        time.sleep(5)
        
        # Klik tombol login
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(5)
        
        # Klik menu My Info
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p').click()
        time.sleep(5)
        
        # Klik submenu Demographics
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[1]/a').click()
        time.sleep(5)
        
        #validasi
        try:
            response_data = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div[2]/div[2]/p').text
            self.assertIn('OrangeHRM', response_data)
            print("TEKS SUDAH SESUAI")
        except NoSuchElementException:
            print("TEKS BELUM SESUAI")
        
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
