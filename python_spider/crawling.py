# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 12:48:40 2018

@author: yatop
"""

import re 
from bs4 import BeautifulSoup


broken_html='<ul class=country><li>Area<li>Population</ul>'
soup=BeautifulSoup(broken_html,'html.parser')
fixed_html=soup.prettify()
print fixed_html

ul=soup.find('ul',attrs={'class':'country'})
ul.find('li')


