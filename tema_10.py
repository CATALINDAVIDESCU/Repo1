# pentru ex (1)
import unittest
from unittest import TestCase
import HtmlTestRunner
from temeSesiunea9 import Test
from intalnirea10Test import CheckBoxTextTest

# pentru ex (2)
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from time import sleep


# (1)

class TestSuite(TestCase):
    def test_suite(self):
        tests = unittest.TestSuite()
        tests.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Test),
                        unittest.defaultTestLoader.loadTestsFromTestCase(CheckBoxTextTest)])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Suite Test: tema 9 + testele intalnirea 10!',
            report_name='Test results',
        )
        runner.run(tests)


# (2)

class TestTema(TestCase):

    def setUp(self):
        self.firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.firefox.get('https://the-internet.herokuapp.com/')
        self.firefox.maximize_window()
        self.firefox.find_element(By.LINK_TEXT, 'Geolocation').click()
        sleep(2)

    def tearDown(self):
        self.firefox.quit()

    def test1_URL(self):
        actual = self.firefox.current_url
        expected = 'https://the-internet.herokuapp.com/geolocation'
        self.assertEqual(expected, actual, 'URL gresit')

    def test2_title(self):
        actual = self.firefox.find_element(By.CSS_SELECTOR, 'h3').text
        expected = 'Geolocation'
        self.assertEqual(expected, actual, 'Titlu gresit')

    def test3_latitude(self):
        self.firefox.find_element(By.CSS_SELECTOR, 'button').click()
        sleep(5)  # => dupa ce dam click pe butonul "Where am i?", acceptam manual accesul la locatia noastra
        text = self.firefox.find_element(By.ID, 'lat-value').text
        text = text.replace('.', '')  # => aici stergem punctul din latitudine pentru a functiona functia .isnumeric()
        actual = text.isnumeric()
        expected = True
        self.assertEqual(expected, actual, 'Fals')

    # faptul ca gasim latitudinea pe ecran ne demonstreaza faptul ca site-ul functioneaza

    def test4_longitudine(self):
        self.firefox.find_element(By.CSS_SELECTOR, 'button').click()
        sleep(5)
        text = self.firefox.find_element(By.ID, 'long-value').text
        text = text.replace('.', '')
        actual = text.isnumeric()
        expected = True
        self.assertEqual(expected, actual, 'Fals')

    def test5_elementalS(self):
        url = self.firefox.find_element(By.LINK_TEXT, 'Elemental Selenium').get_attribute('href')
        actual = url
        expected = 'http://elementalselenium.com/'
        self.assertEqual(expected, actual, 'link gresit')