import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class SmashKartsKeySpammer:
    def __init__(self):
        self.driver = None

    def setup_browser(self):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-logging')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-web-security')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--window-size=1920,1080')
        print('🌐 Starting browser...')
        self.driver = webdriver.Chrome(options=chrome_options)
        print('✅ Browser started!')

    def load_and_spam_keys(self):
        print('[BOT] Navigating to https://smashkarts.io ...', flush=True)
        self.driver.get('https://smashkarts.io')
        time.sleep(10)
        print('[BOT] Spamming random keys!', flush=True)
        keys = [
            Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT,
            'w', 'a', 's', 'd', ' ',  # space
            'q', 'e', 'z', 'x', 'c', 'v', 'b', 'n', 'm'
        ]
        body = self.driver.find_element(By.TAG_NAME, 'body')
        while True:
            key = random.choice(keys)
            body.send_keys(key)
            time.sleep(0.1)

if __name__ == '__main__':
    bot = SmashKartsKeySpammer()
    bot.setup_browser()
    bot.load_and_spam_keys() 