# -*- coding: utf-8-*-

from bs4 import BeautifulSoup
from newsdao import NewsDAO
import requests
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class NewsCrawler(object):
    def __init__(self, url, newsdao):
        self.url = url
        self.newsdao = newsdao

    def get_news_link(self):
        res = requests.get(self.url)
        content = res.content
        soup = BeautifulSoup(content, 'html.parser')

        table = soup.find('div', attrs={'id': 'main_content'})

        for a in table.find_all('a', href=True):
            link = a['href']

            self.get_news_title_contents(link)

    def get_news_title_contents(self, link):
        res = requests.get(link)
        content = res.content
        soup = BeautifulSoup(content, 'html.parser')

        try:
            title = soup.find('h3', attrs={'id': 'articleTitle'}).get_text()
            content = soup.find('div', attrs={'id': 'articleBodyContents'}).get_text()
            content_re = re.sub(r'//.+\n.+{}', '', content)
            content = content_re.strip()
            written_clock = soup.find('span', attrs={'class': 't11'}).get_text()

            newsdao.save_news(link, str(title), str(content), str(written_clock))
        except AttributeError as e:
            print '1'


if __name__ == '__main__':
    url = 'http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105'
    newsdao = NewsDAO()
    URL = NewsCrawler(url, newsdao)
    URL.get_news_link()
