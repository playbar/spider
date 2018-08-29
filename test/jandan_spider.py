import requests
from bs4 import BeautifulSoup

index = 0
headers = {'referer': 'http://jandan.net/', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}

# save pic

def save_jpg(res_url):
    global index
    html = BeautifulSoup(requests.get(res_url, headers=headers).text)
    for link in html.find_all('a', {'class': 'view_img_link'}):
        with open('{}.{}'.format(index, link.get('href')[len(link.get('href'))-3: len(link.get('href'))]), 'wb') as jpg:
            jpg.write(requests.get("http:" + link.get('href')).content)
        print("Crawling section%s data" % index)
        index += 1


if __name__ == '__main__':
    url = 'http://jandan.net/ooxx'
    for i in range(0, 5):
        save_jpg(url)
        url = "http:" + BeautifulSoup(requests.get(url, headers=headers).text).find('a', {'class': 'previous-comment-page'}).get('href')
