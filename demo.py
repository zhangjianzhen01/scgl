from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://192.168.0.217:9900/#/saleInvoice')
driver.quit()