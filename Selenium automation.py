from selenium import webdriver
import time
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\WebDriver\Crome\chromedriver',chrome_options=options)

try:

    driver.get('https://finance.yahoo.com/quote/BTC-USD/history?period1=1410912000&period2=1662336000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true')

    downloadcsv = driver.find_element_by_xpath ("//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[1]/div[2]/span[2]/a")

    downloadcsv.click()

    time.sleep(5)

    driver.close()

except:

     print("Invalid URL")
