from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

class IMDb:
    def __init__(self):
        self.driver = None
        self.wait_timeout = 15

    def initialize_driver(self):
        service = Service(ChromeDriverManager().install())
        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome(service=service)
        self.wait = WebDriverWait(self.driver, self.wait_timeout)

    # Open a website
    def open_website(self, url):
        self.driver.get(url)

    def maximize_window(self):
        self.driver.maximize_window()

#Click the expand button

    def click_expand(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "#__next > main > div.ipc-page-content-container.ipc-page-content-container--center.sc-f9aead43-0.evyTrd > div.ipc-page-content-container.ipc-page-content-container--center > section > section > div > section > section > div:nth-child(2) > div > section > div.ipc-page-grid.ipc-page-grid--bias-left.ipc-page-grid__item.ipc-page-grid__item--span-2 > div.sc-57ba0b6e-0.dyvviw.ipc-page-grid__item.ipc-page-grid__item--span-1 > div > button > span")  # Using CSS selector
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # click the Expand all button
        Expand = self.driver.find_element(By.XPATH, '//span[text()="Expand all"]')

        clicked = False
        for _ in range(3):
            try:
                Expand.click()
                clicked = True
                break
            except Exception as e:
                print(f"Error clicking element: {e}")
                time.sleep(2)

        if not clicked:
            print("Failed to click the element after multiple attempts.")

# Fill the Actor name

    def fill_Name(self, name):
        element = self.driver.find_element(By.XPATH, '(//input[@type="text"])[2]')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


        # Wait for the input field to be present
        enter_name_field =self.driver.find_element(By.XPATH, '(//input[@type="text"])[2]')


        clicked = False
        for _ in range(3):
            try:
                enter_name_field.click()
                clicked = True
                break
            except Exception as e:
                print(f"Error clicking element: {e}")
                time.sleep(2)

        if not clicked:
            print("Failed to click the element after multiple attempts.")

        # Enter the name and press ENTER
        enter_name_field.send_keys(name)
        #enter_name_field.send_keys(Keys.ENTER)

# Fill the Actor day of birth

    def fill_DOB(self, Dob,enddate):

      Enter_Dob_field = self.driver.find_element(By.XPATH, '(//input[@type="text"])[3]')

      Enter_Dob_field.send_keys(Dob)

    # Enter_Dob_field.click()
      Enter_endDob_field = self.driver.find_element(By.XPATH, '(//input[@type="text"])[4]')

      Enter_endDob_field.send_keys(enddate)

    def fill_birthday(self, Dob):

        Enter_Dob_field = self.driver.find_element(By.XPATH, '(//input[@type="text"])[5]')

        Enter_Dob_field.send_keys(Dob)
    # Wait for the name field to be clickable and then click it
        # Enter_birthday_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//input[@type="text"])[5]')))
        # Enter_birthday_field.click()

        # # Click the input field
        # Enter_birthday_field.click()
        #  # Send the date of birth
        # Enter_birthday_field.send_keys(Dob)

    # select_Awards_recognition
    def select_Awards_recognition(self):

        Awards_recognition = self.driver.find_element(By.XPATH, '//*[@id="accordion-item-awardsAccordion"]/div/section/button[1]')
        clicked = False
        for _ in range(3):
            try:
                Awards_recognition.click()
                clicked = True
                break
            except Exception as e:
                print(f"Error clicking element: {e}")
                time.sleep(2)

        if not clicked:
            print("Failed to click the element after multiple attempts.")

#Select the page topic
    def select_Page_topics(self):

        # select_Page_topics
        Page_topics = self.driver.find_element(By.XPATH, '//*[@id="accordion-item-pageTopicsAccordion"]/div/div/section/button[1]')
        clicked = False
        for _ in range(3):
            try:
                Page_topics.click()
                clicked = True
                break
            except Exception as e:
                print(f"Error clicking element: {e}")
                time.sleep(2)

        if not clicked:
            print("Failed to click the element after multiple attempts.")

     #choose the gender
    def select_gender(self):
        gender = self.driver.find_element(By.XPATH,'//*[@id="accordion-item-genderIdentityAccordion"]/div/section/button[1]')
        clicked = False
        for _ in range(3):
            try:
                gender.click()
                clicked = True
                break
            except Exception as e:
                print(f"Error clicking element: {e}")
                time.sleep(2)

        if not clicked:
            print("Failed to click the element after multiple attempts.")

# Enter the film name
    def credits(self,credit):
        credits = self.driver.find_element(By.XPATH, '//*[@id="accordion-item-filmographyAccordion"]/div/div/div/div[1]/input')

        credits .send_keys(credit)

        credits.send_keys(Keys.ENTER)


    def close_browser(self):
        if self.driver:
            self.driver.quit()


#create a class instance
imdb = IMDb()
# initialize the driver
imdb.initialize_driver()
#Lunch the url
imdb.open_website("https://www.imdb.com/search/name/")
#maximize the window
imdb.maximize_window()
imdb.driver.implicitly_wait(10)
#click the expand button
imdb.click_expand()
# Enter the actor name in name feild
imdb.fill_Name("Vijay")
imdb.driver.implicitly_wait(10)
# enter Acotor DOB
imdb.fill_DOB("1974-06","1974-07")
imdb.driver.implicitly_wait(10)
imdb.fill_birthday("06-22")
#Select the Award_recognition
imdb.select_Awards_recognition()
#Select the page topics
imdb.select_Page_topics()
#select the gender
imdb.select_gender()
#Enter the actor film in credits filed
imdb.credits("Naalaiya Theerpu")
#Close the browser
imdb.close_browser()


