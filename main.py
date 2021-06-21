from selenium import webdriver

chrome_driver_path = "C:\\Development\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com/430-G3-i3-6100U-%E9%9B%99%E6%A0%B8%E5%BF%83%E8%99%95%E7%90%86%E5%99%A8-Windows/dp/B08P4NXTSG/ref=sr_1_1_sspa?dchild=1&keywords=mac+book&qid=1624257252&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExWUpVUjZBSDhEQjlPJmVuY3J5cHRlZElkPUEwNzUyOTgxMU1CSkZKVExQQjBOTSZlbmNyeXB0ZWRBZElkPUEwNzA0NzkxMzNLRjhTSlJXUEoxNyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")
price = driver.find_element_by_id("priceblock_saleprice")
print(price.text)


# driver.close()
# driver.quit()
