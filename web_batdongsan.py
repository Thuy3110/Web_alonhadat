from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("detach= True")
driver = webdriver.Chrome(options=options)

data =[]

for page in range(1,6):
    url = f"https://alonhadat.com.vn/nha-dat/cho-thue/nha-dat/3/da-nang/trang--{page}.html"
    driver.get(url)

    time.sleep(5)
    lists = driver.find_elements (By.XPATH, '//div[contains(@class, "content-item")]')

    for listing in lists:
        try:
            title = listing.find_element (By.XPATH, './/div[@class="ct_title"]/a').text
            try:
                description = listing.find_element (By.XPATH, '//*[@id="left"]/div[1]/div[1]/div[4]/div[1]').text
            except:
                description= "Không có mô tả"
            try:
                area = listing.find_element(By.XPATH,'.//div[@class="ct_dt"]').text
            except:
                area =" Không có diện tích xác định"
            try:
                address= listing.find_element(By.XPATH,'.//div[@class="ct_dis"]').text
            except:
                address=" không cập nhật địa chỉ"
            try:
                price = listing.find_element(By.XPATH,'.//div[@class="ct_price"]').text
            except:
                price =" Không cập nhật giá"
            data.append([title, description, area, price, address])

        except Exception as e:
            print ("Bị lỗi khi lyaas dữ liệu", e)

driver.quit()

df = pd.DataFrame(data, columns= ['Tiêu đề', 'Mô tả', 'Diện tích', 'Giá', 'Địa chỉ'])

df.to_excel (r"D:\Thuy\Tu Dong Hoa\BTL\alonnhadat_dn.xlsx",index =False)
print (" Data đã lưu và file Excel thành công")
