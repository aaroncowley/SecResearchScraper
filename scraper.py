
import time
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://apps.webofknowledge.com/summary.do?product=WOS&parentProduct=WOS&search_mode=GeneralSearch&qid=1&SID=5AMkc7rK32QEqeo4cm7&page=1&action=changePageSize&pageSize=1000');
time.sleep(5)

resultElement = driver.find_element(by='id', value='hitCount.top')
resultNum = resultElement.text
print(resultNum)
for i in range(resultNum):
    
    

driver.quit()
