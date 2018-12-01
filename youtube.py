from selenium import webdriver
from lxml import etree
from lxml import html
import time


# use chrome webdriver, already downloaded, put in the same directory
driver = webdriver.Chrome()

# single video url here
driver.get("https://www.youtube.com/watch?v=Te-EQdku9PI")


########  parse

def scrollDown(pause, driver):

    last_location = 0

    time_pass_4 = False
    time_pass_6 = False

    time.sleep(3)
    driver.execute_script("window.scrollTo(0,800);")
    time.sleep(3)

    

    while True:
        driver.execute_script("window.scrollTo(0, window.scrollY + 2200);")
        time.sleep(pause)
        cur_location = driver.execute_script("return window.scrollY")
        print("last_location  : ")
        print(last_location)
        
        print("cur_location :  ")
        print(cur_location)


        if cur_location == last_location:
            if not time_pass_4:
                time_pass_4 = True
                continue
            else:
                if time_pass_6:
                    break
                else:
                    time_pass_6 = True
                    continue
        last_location = cur_location
        

#scroll every 2 seconds, wait for 6 seconds at most
scrollDown(2, driver)

page = driver.page_source

#page source parsed will be in current_page.txt
with open('current_page.txt', 'w', encoding = "utf8") as write_file:
    write_file.write(page)



###### read and analyse

#read from page source
page_source = ""
with open('current_page.txt', 'r', encoding = "utf8") as read_file :
    page_source = read_file.read()

html_content = html.fromstring(page_source)

list_of_comments = html_content.xpath('//yt-formatted-string[@id="content-text"]/text()')

with open('comments.txt','w', encoding = "utf8") as write_file:
    for comment in list_of_comments :
        write_file.write(comment[:-1]+";;;")   # ;;; is the splitter, slide the string to remove mysterious endofline character






