import requests
from  bs4 import  BeautifulSoup
import json


raw_data = []
raw_json = {}
url = 'https://en.wikipedia.org/wiki/Selenium_(software)'

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0"
}

source = requests.get(url,headers=header)
data = source.text

soup_html = BeautifulSoup(data, 'html.parser')
#print("Using html.parser:")
#print(soup_html.prettify())

find_data =  soup_html.find('div', class_='mbox-text-span')
data = find_data.text
my_data_item = {'text': data}
my_final_data_item = raw_data.append(my_data_item)
print(raw_data)

with open('test.json', 'w', encoding='utf-8') as fp:
    json.dump(raw_data, fp, indent=4)


'''for hrefs in find_data:
    get_href = soup_html.find('pre')
    get_span = get_href.find_all('span')
    for text in get_span:
        print(text.text)'''


