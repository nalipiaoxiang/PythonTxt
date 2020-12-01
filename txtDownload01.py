import requests
import jsonpath
from lxml import etree

url = 'http://www.iddwx.com/soft1/'
url = 'http://www.iddwx.com/soft2/'

response = requests.get(url)
content = response.content.decode('UTF-8')
# print(content)
html = etree.HTML(content)

txt_name_list = html.xpath('/html/body/div[@class="globalBox"]/div[@id="pageMain"]/div[@class="mainBody"]/div[@class="pageMainArea"]/div[@id="listbox"]/ul[@id="mainlistUL"]/div[@class="mainListInfo"]/div/span/a')
txt_size_list = html.xpath('/html/body/div[@class="globalBox"]/div[@id="pageMain"]/div[@class="mainBody"]/div[@class="pageMainArea"]/div[@id="listbox"]/ul[@id="mainlistUL"]/div[@class="mainListBottom"]/div[@class="mainAccredit"]/text()')
txt_introduction_list = html.xpath('/html/body/div[@class="globalBox"]/div[@id="pageMain"]/div[@class="mainBody"]/div[@class="pageMainArea"]/div[@id="listbox"]/ul[@id="mainlistUL"]/div[@id="soft_content_1"]/text()')
# print(type(txt_name_list))


#文本详情
txt_info_list = [href_title.attrib for href_title in txt_name_list]

#将文件大小加入
i=0
for info in txt_info_list:
    info['size'] = txt_size_list[i]
    info['introduction'] = txt_introduction_list[i]
    i+=1
# print(txt_info_list)

#去除小于3MB

#1.带有KB的删掉
with_KBs = [info for info in txt_info_list if info.get('size').endswith('KB')]
# for data in with_KBs:
#     print(data)

for with_KB_data in with_KBs:
    txt_info_list.remove(with_KB_data)

#2.小于3MB的删掉
lt_3MBs = [info for info in txt_info_list if int(info.get('size').split('.')[0]) < 3]

for lt_3MB_data in lt_3MBs:
    txt_info_list.remove(lt_3MB_data)






# print(len(txt_info_list))


print('---------------------------')
for data in  txt_info_list:
    print(data)

# for b in txt_size_list:
#     print(b)








print('执行结束')



