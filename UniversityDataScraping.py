from selenium import webdriver
from time import time, sleep
import pandas as pd
from openpyxl import Workbook
import time

driver = webdriver.Chrome(executable_path="C:\\seleniumbrowserdriverSave\\chromedriver.exe")
driver.get("https://www.turkiye.gov.tr/universite-hizmet-listesi")
time.sleep(3)
# Bu kısımda webdriverımızı açıyoruz. get komutu ile de veri çekmek istediğimiz siteye gidiyoruz.

for i in range(1, 173):
    uni_path = f"//*[@id='agencyListBlock']/li[{i}]/div/div/h3/a"
    uni_name = driver.find_element_by_xpath(uni_path).text
    print(uni_name)
    time.sleep(0.25)

# // *[ @ id="agencyListBlock"] / li[1] / div / div / h3 / a
# // *[ @ id="agencyListBlock"] / li[2] / div / div / h3 / a
# Bu kısımda da gördüğümüz gibi li[i] kısmında bulunan i değerimiz değişiklik göstermektedir.
# Bu değişiklik gösteren i değerine göre üniversitelerin sıralamasını yaptırmaktayız.

wb = Workbook()
wb['Sheet'].title = "Report"
sh1 = wb.active

for i in range(1, 173):
    sh1[f'A{i}'].value = f"Üniversite:{i} "
    sh1[f'B{i}'].value = driver.find_element_by_xpath(f"//*[@id='agencyListBlock']/li[{i}]/div/div/h3/a").text
    wb.save(r"C:\\Users\\Murat Can Özen\\Desktop\\dovizIslemEx.xlsx")
driver.close()

# Bu kısımda internet üzerinden çekmiş olduğumuz üniversite bilgilerini belirtmiş
# olduğumuz isimli excel dosyasına yazmaktayız.
