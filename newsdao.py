# -*- coding: utf-8 -*-

from model import News
from connection import Session
import datetime as dt
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class NewsDAO(object):
    def __init__(self):
        pass

    def save_news(self, news_id, title, content, written_clock):
        saved = False
        session = Session()
        if not self.get_news_by_id(news_id):
            print news_id
            news = News(link=news_id, title=title, contents=content,
                        written_time=written_clock, crawl_time=dt.datetime.now())
            session.add(news)
            session.commit()
            saved = True

        session.close()

        return saved

    def get_news_by_id(self, news_id):
        try:
            session = Session()
            row = session.query(News) \
                .filter(News.link == news_id) \
                .first()

            return row
        except Exception as e:
            print e
        finally:
            session.close()

    def get_news_contents_by_id(self, news_id):
        try:
            session = Session()
            row = session.query(News) \
                .filter(News.link == news_id) \
                .first()

            return row.contents
        except Exception as e:
            print e
            return ''
        finally:
            session.close()

    def get_news_by_keyword_in_title(self, keyword):
        data = []
        session = Session()
        result = session.query(News).filter(News.title.like('%' + keyword + '%')).all()
        for row in result:
            news = {}
            news['link'] = row.link
            news['title'] = row.title
            news['written_time'] = row.written_time

            data.append(news)
        return data

    def get_news_by_keyword_in_content(self, keyword):
        data = []
        session = Session()
        result = session.query(News).filter(News.contents.like('%' + keyword + '%')).all()
        for row in result:
            news = {}
            news['link'] = row.link
            news['title'] = row.title
            news['content'] = row.contents
            news['written_time'] = row.written_time

            data.append(news)
        return data
