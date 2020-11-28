import requests
import jsonpath
from lxml import etree

url = 'http://www.iddwx.com/soft1/'

response = requests.get(url)
content = response.content.decode('UTF-8')
print(content)
html = etree.HTML(content)

text_name_list = html.xpath('/html/body/div[@class="globalBox"]/div[@id="pageMain"]/div[@class="mainBody"]/div[@class="pageMainArea"]/div[@id="listbox"]/ul[@id="mainlistUL"]/div[@class="mainListInfo"]/div/span/a')
text_size_list = html.xpath('/html/body/div[@class="globalBox"]/div[@id="pageMain"]/div[@class="mainBody"]/div[@class="pageMainArea"]/div[@id="listbox"]/ul[@id="mainlistUL"]/div[@class="mainListBottom"]/div[@class="mainAccredit"]/text()')



# for a in text_name_list:
#     print(a.attrib)

text_info = [href_title.attrib for href_title in text_name_list]

i=0
for info in text_info:
    info['size'] = text_size_list[i]
    i+=1



print(text_info)

# for b in text_size_list:
#     print(b)








print('执行结束')



