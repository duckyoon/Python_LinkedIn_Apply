from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time
from dotenv import load_dotenv
import os

load_dotenv()

USER_ID = os.getenv("ID")
USER_PWD = os.getenv("PWD")
# print(USER_ID)

# 설정
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


url = "https://www.linkedin.com/search/results/all/?keywords=python%20web%20developer&origin=AUTO_COMPLETE&searchId=4e820722-ecc7-40b8-b68e-103ee018fdc8&spellCorrectionEnabled=false"


driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

time.sleep(3)

# 로그인 버튼 클릭
# login = driver.find_element(By.CSS_SELECTOR, ".nav__button-secondary")
# login.click()
# time.sleep(5)

# 구글 로그인 클릭
# google_login = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[2]/span[1]')
# google_login.click()

# 로그인 정보 입력?
user_id = driver.find_element(By.ID, 'username')
user_id.click()
user_id.send_keys(USER_ID)
time.sleep(1)
user_pwd = driver.find_element(By.ID, 'password')
user_pwd.click()
user_pwd.send_keys(USER_PWD)
time.sleep(2)
# user_pwd.send_keys(Keys.Enter)

login_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
login_button.click()
time.sleep(3)
# # 채용공고 모두보기 클릭
# view_all_job = driver.find_element(By.XPATH, '//*[@id="yzVil46+Ttq2CEQJAu/1Og=="]/div/div[2]/a')
# view_all_job.click()
# time.sleep(3)

apply = driver.find_element(By.CLASS_NAME, 'WbGDmmqxNQkLHmYIoCaviwkIDgSiAHeUzhtQFNmg')
apply.click()
time.sleep(3)

# 공고 목록 추가
item_all = driver.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list-container li")
item_id = [item.get_attribute('id') for item in item_all]
print(item_id)

# 순서별로 클릭하여 모든 공고 저장
try:
    for item in item_id:
        if item != '':
            select = driver.find_element(By.ID, f"{item}")
            select.click()
            time.sleep(1)
            save = driver.find_element(By.CSS_SELECTOR, ".mt5 .display-flex .jobs-save-button")
            save.click()
            time.sleep(1)
except NoSuchElementException:
    print("There is no possible job application")
    
    
time.sleep(3)    
driver.quit()


# save = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[5]/div/button')
# save.click()



