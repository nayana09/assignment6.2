from selenium import webdriver
from selenium import webdriver


from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")

option.add_argument("start-maximized")

option.add_argument("--disable-extensions")

option.add_experimental_option("prefs",
{"profile.default_content_setting_values.notifications": 2
 })
driver = webdriver.Chrome(options=option,executable_path="C:\Program Files (x86)\chromedriver.exe")

driver.get("https://www.ajio.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_xpath("//input[@name='searchVal']").send_keys("shoes")
driver.find_element_by_xpath("//button[@type='submit']").click()
driver.find_element_by_xpath("//*[@id='products']/div[3]/div[1]/div/div[1]/a/div/div[1]/img").click()
handles = driver.window_handles
size = len(handles)
for x in range(size):
  driver.switch_to.window(handles[x])
driver.find_element_by_xpath("//div[contains(text(),'8')]").click()
driver.find_element_by_xpath("//*[@id='appContainer']/div[2]/div/div/div[2]/div/div[3]/div/div[9]/div[1]/div[1]/div").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//*[@id='appContainer']/div[2]/div/div/div[2]/div/div[3]/div/div[9]/div[1]/div[1]/a/div").click()
#done succesfully