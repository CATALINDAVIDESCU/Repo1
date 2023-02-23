from time import sleep

import self as self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager import chrome

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# class Selectori:
#     chrome = webdriver.Chrome()
#
#     def __init__(self):
#        #self.chrome.get('https://www.techlistic.com/p/selenium-practice-form.html/form')
#         self.chrome.maximize_window()

    #
    #
    #      def __init__(self):
    #           self.chrome.get('https://mail.yahoo.com')
    #           self.chrome.maximize_window()

    # find element by id

    # def elementByID(self,ID):
    #      loginUsername =self.chrome.find_element(By.ID,f'{ID}')
    #      loginUsername.send_keys('Cata')
    #      sleep(4)

    # def elementByID(self,ID):
    #       self.chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
    #       self.chrome.find_element(By.ID,f'{ID}').send_keys('Australia')
    #       sleep(5)

    # def elementByID(self,ID):
    #      self.chrome.get('https://the-internet.herokuapp.com/')
    #      self.chrome.find_element(By.ID,f'{ID}')
    #      sleep(4)

    # def element by name

    # def elementByName(self,name):
    #      self.chrome.get('https://mail.yahoo.com')
    #      self.chrome.find_element(By.NAME,f'{name}').send_keys('Cata')

    # def elementByName(self,name):
    #      self.chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
    #      self.chrome.find_element(By.NAME,f'{name}').send_keys('Cata')
    #      sleep(2)

    # def elementByName(self,name):
    #      self.chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
    #      self.chrome.find_element(By.NAME,f'{name}').send_keys('Davidescu')
    #      sleep(3)

    # def elementByCSS(self,css):„„sleep(2)

    # print(cssSelector.location)
    #      def __init__(self):
    #           self.chrome.get('https://mail.yahoo.com')
    #           self.chrome.maximize_window()

    # def elementByCSS(self,Id):
    #      self.chrome.get('https://mail.yahoo.com')
    #      self.chrome.find_element(By.CSS_SELECTOR(f'{ID}'))

    # def elementByCSS(self,Class):
    #      self.chrome.get('https://mail.yahoo.com')
    #      self.chrome.find_element(By.CSS_SELECTOR,f'{Class}')

    # find element by link text

    # def elementByLinkText(self, linkTxt):
    #      self.chrome.get('https://phptravels.net/')
    #      self.chrome.find_element(By.LINK_TEXT,f'{linkTxt}').click()
    #
    #      sleep(4)

    # def elementByLinkText(self,linkTxt):

    #      self.chrome.get('https://phptravels.net/')
    #      self.chrome.find_element(By.LINK_TEXT,f'{linkTxt}').click()
    #      sleep(4)

    # def elementByLinkText(self,linkTxt):
    #      self.chrome.get('https://the-internet.herokuapp.com/')
    #      self.chrome.find_element(By.LINK_TEXT,f'{linkTxt}').click()
    #      sleep(4)

    # find element by partial link

    # def elementByPartialLinkText(self,linkTxt):
    #      self.chrome.get('https://the-internet.herokuapp.com/')
    #      self.chrome.find_element(By.PARTIAL_LINK_TEXT,f'{linkTxt}').click()
    #      sleep(3)

    # def elementByPartialLinkText(self, linkTxt):
    #      self.chrome.get('https://www.emag.ro/')
    #      self.chrome.find_element(By.PARTIAL_LINK_TEXT,f'{linkTxt}').click()
    #      sleep(3)

    # def elementByPartialLinkText(self,linkTxt):
    #      self.chrome.get('https://www.itfactory.ro/')
    #      self.chrome.find_element(By.PARTIAL_LINK_TEXT,f'{linkTxt}').click()
    #      sleep(4)

    # find selector by tag_name
    #chrome = webdriver.Chrome()

    # def __init__(self):
    #     self.chrome.get('https://jules.app/sign-in')
    #     self.chrome.maximize_window()
    #
    #     self.chrome.get('https://phptravels.net/login')
    #     input_list = chrome.find_element(By.TAG_NAME, 'h4.info_title').click()
    #     sleep(5)
    #     chrome.quit()

    # def elementByTagName(self):
    #     self.chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
    #     self.chrome.find_element(By.TAG_NAME,'input')
    #     self.chrome.send_keys1('Catalin')
    #     self.chrome.implicitly_wait(2)
    #





#test=Selectori()
# test.elementByID('login-username')
# test.elementByName('username')
# test.elementByCSS('#login-username')
# test.elementByName('firstname')
# test.elementByName('lastname')
# test.elementByID('continents')
# test.elementByID('content')
# test.elementByLinkText('Visa')
# test.elementByLinkText('Transfers')
# test.elementByLinkText('Drag and Drop')
# test.elementByPartialLinkText('Brok')
# test.elementByPartialLinkText('Laptop')
# test.elementByPartialLinkText('Despre noi')


#CLASS_NAME SELECTOR
#class Demo_find_elementByClassName():
    #def locate_by_class_name_demo(self):
        #driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        #driver.maximize_window()
        # driver.get('https://www.emag.ro/')
        # driver.find_element(By.CLASS_NAME,'js-login-btn').send_keys('catalin')
        # driver.implicitly_wait(4)

        # driver.get('https://legal.yahoo.com/ie/ro/yahoo/privacy/index.html')
        # element = driver.find_element(By.CLASS_NAME,"privacy").click()
        # driver.implicitly_wait(3)


#Find element by xpath
s= Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
#Dupa atribut - valoare

#chrome.get('https://phptravels.net/signup')
#chrome.find_element(By.XPATH,'//input[@type="text"]').send_keys('DAVIDESCU')
#chrome.get('https://phptravels.net/login')
#chrome.find_element(By.XPATH,'//input[@type="email"]').click()
#chrome.find_element(By.XPATH,'//input[@type="password"]').send_keys('2233')


#Dupa textul de pe element

#chrome.get('https://the-internet.herokuapp.com/')
#chrome.find_element(By.XPATH,'//a[text()="Broken Images"]').click()
#chrome.get('https://www.dedeman.ro/')
#chrome.find_element(By.XPATH,'//a[text()="Recomandarile saptamanii"]').click()
#chrome.get('https://www.prosport.ro/')
#chrome.find_element(By.XPATH,'//a[text()="Tenis"]').click()

#Dupa partial text

#chrome.get('https://www.prosport.ro/cupa-mondiala-qatar-2022')
#chrome.find_element(By.XPATH,'//a[contains(text(),"Mondial")]').click()

#Folosind pipe

#chrome.get('https://ro-ro.facebook.com/')
#chrome.find_element(By.XPATH, '//input[@type="text"] | //a[@type="text"]').send_keys("cuminede18")

#Folosind *
#chrome.get('https://www.emag.ro/cart/products?ref=cart')
#chrome.find_element(By.XPATH, '//*[@id="my_cart"]').click()

#Folosind parent::

#chrome.get('https://www.dedeman.ro/')
#chrome.find_element(By.XPATH,'//li[@class ="position-relative"]/parent::ul').click()

#Folosind fartele anterior sau de dupa

# chrome.get('https://www.emag.ro/')
# chrome.find_element(By.XPATH,'//li[@data-id="23"]/following-sibling::li[2]').click()
# sleep(4)
# chrome.quit()