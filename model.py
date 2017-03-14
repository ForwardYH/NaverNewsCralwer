# -*- coding: utf-8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from sqlalchemy import Column, ForeignKey, Integer, CHAR, Date, String, Time, Index, DateTime, TIMESTAMP, func
from sqlalchemy.dialects.mysql import INTEGER, BIT, TINYINT, TIME, DOUBLE, LONGTEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class News(Base):
    __tablename__ = 'News'

    link = Column(String(200), primary_key=True, nullable=False)
    title = Column(String(100), nullable=False)
    contents = Column(LONGTEXT, nullable=False)
    written_time = Column(DateTime, nullable=False)
    crawl_time = Column(DateTime, nullable=False)
