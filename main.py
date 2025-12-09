import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv


#Load environment variables from .env file
load_dotenv()
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
SIMILAR_ACCOUNT = os.getenv("SIMILAR_ACCOUNT")




class InstaFollower:
    def __init__(self):
        #Chrome options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        """Logs into Instagram using credentials from .evn"""
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(4.2) #wait for page to load

        #Find username and password fields and enter credentials
        username_entry = self.driver.find_element(By.NAME, "username")
        username_entry.send_keys(USERNAME)
        password_entry = self.driver.find_element(By.NAME, "password")
        password_entry.send_keys(PASSWORD)
        password_entry.send_keys(Keys.ENTER) #press Enter key

        time.sleep(10) #wait for login to complete

        #Click "Not Now" button if it appears (for saving login info)
        not_now_button = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Şimdi değil')]")
        if not_now_button:
            not_now_button.click()

    def find_followers(self):
        """Opens the followers list of a similar account and scrolls"""
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        wait = WebDriverWait(self.driver, 10)

        #Find the followers button and click it
        followers_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/followers/')]"))
        )
        followers_button.click()
        time.sleep(5.6)

        #Find the scrollable followers popup
        scroll_box = self.driver.find_element(
            By.XPATH,
            '//div[@role="dialog"]//div[@class="x6nl9eh x1a5l9x9 x7vuprf x1mg3h75 x1lliihq x1iyjqo2 xs83m0k xz65tgg x1rife3k x1n2onr6"]'
        )
        #Scroll the followers box to load more followers
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",scroll_box)
            time.sleep(2)


    def follow(self):
        """Follows users from the loadede followers list (currently empty)"""
        pass


#Run the bot
bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()