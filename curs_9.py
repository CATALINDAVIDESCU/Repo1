import webdriver_manager
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from unittest import TestCase


def send_keys(param):
    pass


class Test(TestCase):
    def setUp(self):
        self.chrome = webdriver.Chrome(ChromeDriverManager().install())
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.maximize_window()

    def tearDown(self):
        self.chrome.quit()

    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://phptravels.net/'
        self.assertEqual(expected, actual, 'Url incorect')

    # def testSearchByCity(self):
    #     self.chrome.implicitly_wait(2)
    #     searchbar = self.chrome.find_element(By.ID,'select2-hotels_city-container')
    #     searchbar.click()
    #     search1= self.chrome.find_element(By.CLASS_NAME,'select2-hotels__field')
    #     search1 =send_keys('Bucharest')
    #     self.chrome.implicitly_wait(3)
    #     expectedValue = 'Bucharest, Romania'
    #     result = self.chrome.find_element(By.CLASS_NAME,'select2-resuts__option select-results__option--highlighted')
    #     actual = result.text
    #     self.assertEqual(expectedValue,actual,'Rezultat incorect')

    def test_addremovelinktxt_url(self):
        self.chrome.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/add_remove_elements'
        self.assertEqual(expected, actual, 'Url incorect')

    def test_header_addremoveelement(self):
        self.chrome.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        actual= self.chrome.find_element(By.CSS_SELECTOR, 'h3').text
        expected = 'Add/Remove Elements'
        self.assertEqual(expected, actual, "text incorect")

    def test_press_addelementbutton(self):
        self.chrome.find_element(By.LINK_TEXT,'Add/Remove Elements').click()
        self.chrome.find_element(By.CSS_SELECTOR,'button').click()
        actual = self.chrome.find_element(By.ID,"elements").text
        expected ='Delete'
