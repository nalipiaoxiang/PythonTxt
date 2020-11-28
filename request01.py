import requests

url = 'http://www.baidu.com'
# url = 'http://www.iddwx.com/soft1/'


response = requests.get(url)

#编码格式
print(response.encoding)

# 字符集设定 ISO-8859-1,UTF-8,utf8
response.encoding = 'UTF-8'
response.encoding = 'utf8'

# print(response.text)

#response.content byte类型的数据
# print(response.content)


#response.content.decode('字符集编码') --解码操作 从byte到字符串
# print(response.content.decode('ISO-8859-1'))

print(response.encoding)

#响应url
print(response.url)

#状态码
print(response.status_code)

#请求头
print(response.request.headers)

#响应头
print(response.headers)

#cookie
print(response.cookies)

#长度
print(len(response.content))