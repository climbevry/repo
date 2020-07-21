# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 16:59:07 2020

@author: adanilina
"""

import sys
import requests #https://realpython.com/python-requests/
from requests.exceptions import HTTPError
import cx_Oracle
import xmltodict
from pprint import pprint
import codecs

url = r'C:\Users\adanilina\Desktop\Персей ЧТЗ\network_orig.xml'
#with open(r'C:\Users\adanilina\Desktop\Персей ЧТЗ\network_orig.xml', encoding='utf8') as fd:
#doc = fd.read()
# doc = xmltodict.parse(fd.read())
 
with codecs.open(url, 'r', encoding='utf8') as file:
 doc = xmltodict.parse(file.read())  

pprint(doc)