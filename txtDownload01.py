import requests
import jsonpath
from lxml import etree

url = 'http://www.iddwx.com/soft1/'

response = requests.get(url)
content = response.content.decode('UTF-8')
# print(content)
html = etree.HTML(content)

txt_name_list = html.xpath('/html/body/div[@class="globalBox"]/div[@id="pageMain"]/div[@class="mainBody"]/div[@class="pageMainArea"]/div[@id="listbox"]/ul[@id="mainlistUL"]/div[@class="mainListInfo"]/div/span/a')
txt_size_list = html.xpath('/html/body/div[@class="globalBox"]/div[@id="pageMain"]/div[@class="mainBody"]/div[@class="pageMainArea"]/div[@id="listbox"]/ul[@id="mainlistUL"]/div[@class="mainListBottom"]/div[@class="mainAccredit"]/text()')
# print(type(txt_name_list))

# for a in txt_name_list:
#     print(a.attrib)


# for a in txt_name_list:
#     print(a.attrib)

#文本详情
txt_info_list = [href_title.attrib for href_title in txt_name_list]

#将文件大小加入
i=0
for info in txt_info_list:
    info['size'] = txt_size_list[i]
    i+=1

print(len(txt_info_list))

for info in txt_info_list:
    if info.get('size').endswith('KB'):
        txt_info_list.remove(info)
print('---------------------------')
print(len(txt_info_list))


# print(txt_info)

# for b in txt_size_list:
#     print(b)








print('执行结束')



