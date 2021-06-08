from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
import time

CHROME_DRIVER_PATH = "Import your chrome driver here"
FRD_ACC = "Your Friend Acc"
USERNAME = "Your Email"
PASSWORD = "Your password"


class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        user_id = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        user_pw = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        login_btn = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        user_id.send_keys(USERNAME)
        user_pw.send_keys(PASSWORD)

        time.sleep(2)
        login_btn.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{FRD_ACC}")

        time.sleep(3)
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        followers.click()

        time.sleep(3)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(3)

    def follow(self):
        all_btns = self.driver.find_elements_by_css_selector("li button")
        for btn in all_btns:
            try:
                btn.click()
                time.sleep(3)
            except ElementClickInterceptedException:
                cancel_btn = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_btn.click()
                time.sleep(1)



bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
