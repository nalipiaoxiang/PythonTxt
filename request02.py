import requests

url = 'http://www.baidu.com'

response = requests.get(url)

print(len(response.content))

#带heads
heads = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}
response1 = requests.get(url,headers=heads)
print(response1.content)
print(len(response1.content))