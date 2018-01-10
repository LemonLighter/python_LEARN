# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 12:48:40 2018

@author: yatop
"""

import re 
from bs4 import BeautifulSoup

FIELDS = ('area','population','iso','country','capital','continent',
          'tld','currency_code','currency_name','phone','postal_code_format',
          'postal_code_regex','languages','neighbbours')

def re_scraper(html):
    results={}
    for field in FIELDS:
        results[field]=re.search('<tr id="places_%s__row">')

broken_html='<ul class=country><li>Area<li>Population</ul>'
soup=BeautifulSoup(broken_html,'html.parser')
fixed_html=soup.prettify()
print fixed_html

ul=soup.find('ul',attrs={'class':'country'})
ul.find('li')


import lxml.html
broken_url='<ul class=country><li>Area<li>Population</ul>'
tree=lxml.html.fromstring(broken_url)
fixed_url=lxml.html.tostring(tree,pretty_print=True)
print fixed_url