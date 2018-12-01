from lxml import etree
from lxml import html

page_source = ""
with open('current_page.txt', 'r', encoding = "utf8") as read_file :
    page_source = read_file.read()

# page_source.encode("ascii","ignore")

html_content = html.fromstring(page_source)

result = html_content.xpath('//yt-formatted-string[@id="content-text"]/text()')

with open('result.txt','w', encoding = "utf8") as write_file:
    for s in result :
        write_file.write(s[:-1]+"\n")