from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("detach= True")
driver = webdriver.Chrome(options=options)

data =[]

start_url = f"https://alonhadat.com.vn/nha-dat/cho-thue/nha-dat/3/da-nang/trang--1.html"
driver.get(start_url)
time.sleep(5)

page = 0
while True:
    page = page + 1
    url = f"https://alonhadat.com.vn/nha-dat/cho-thue/nha-dat/3/da-nang/trang--{page}.html"
    print (f"Đang lấy dữ liệu từ trang {page}")
    driver.get(url)
# sử dụng webDriverWait khi trang họ bắt xn ko phải robot thì nó vẫn chờ mà ko thoát luôn
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "content-item"))
        )
    except:
        print(f" Ko thể tìm phân trang {page}")
        continue
    # time.sleep(5) // nó sẽ thoát ngay khi hiện xác thực bạn ko phải robot

    lists = driver.find_elements (By.CLASS_NAME, "content-item")
    if not lists :
        print (f"Không còn tin naò ở trang {page}")
        break

    for listing in lists:
        try:
            title = listing.find_element (By.XPATH, './/div[@class="ct_title"]/a').text
            try:
                description = listing.find_element (By.XPATH, './/div[contains(@class,"ct_desciption")]').text
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
            print ("Bị lỗi khi lấy dữ liệu", e)

driver.quit()

df = pd.DataFrame(data, columns= ['Tiêu đề', 'Mô tả', 'Diện tích', 'Giá', 'Địa chỉ'])

df.to_excel (r"D:\Thuy\Tu Dong Hoa\BTL\alonnhadat_dn.xlsx",index =False)
print (" Data đã lưu và file Excel thành công")
