from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from dotenv import load_dotenv
import os

load_dotenv()

USER_ID = os.getenv("ID")
USER_PWD = os.getenv("PWD")

# 설정
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

url = "https://www.linkedin.com/jobs/search?keywords=python&location=%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%20%EC%84%9C%EC%9A%B8%20%EC%84%9C%EC%9A%B8&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"


driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

time.sleep(5)

# 로그인 버튼 클릭
login = driver.find_element(By.CSS_SELECTOR, ".nav__button-secondary")
login.click()
time.sleep(5)

# 구글 로그인 클릭
google_login = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[2]/span[1]')
google_login.click()

# 로그인 정보 입력
user_id = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
user_id.click()
user_id.send_keys(USER_ID)


user_pwd = driver.find_element(By.ID, "password")
time.sleep(1)

# 

# user_id.click()
# time.sleep(1)
# user_id.send_keys(USER_ID)
# time.sleep(1)

# user_pwd.click()
# time.sleep(1)
# user_pwd.send_keys(USER_PWD)
# time.sleep(1)

# login_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
# login_button.click()

# <button class="btn__primary--large from__button--floating"
# data-litms-control-urn="login-submit"
# aria-label="로그인"
# type="submit">
#               로그인
#           </button>