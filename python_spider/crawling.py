# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 12:48:40 2018

@author: yatop
"""

import re 
from bs4 import BeautifulSoup
import lxml.html
import csv

FIELDS = ('area','population','iso','country','capital','continent',
          'tld','currency_code','currency_name','phone','postal_code_format',
          'postal_code_regex','languages','neighbbours')

def re_scraper(html):
    results={}
    for field in FIELDS:
        results[field]=re.search('<tr id="places_%s__row">.?*<td class="w2p_fw">(.*?)</td>' % field,html).groups()[0]
    return results

def bs_scraper(html):
    soup=BeautifulSoup(html,'html.parser')
    results={}
    for field in FIELDS:
        results[field]=soup.find('table').find('tr',id='places_%s__row' % field).find(
                'td',class_='w2p_fw').text
    return results

def lxml_scraper(html):
    tree=lxml.html.fromstring(html)
    results={}
    for field in FIELDS:
        results[field]=tree.cssselect('table > tr#places_%s__row> td.w2p_fw' % field)[0].text_content()
        return results

class ScrapeCallback:
    def __init__(self):
        self.writer=csv.writer(open('countries.csv','w'))
        self.fields=('area','population','iso','country','capital','continent',
          'tld','currency_code','currency_name','phone','postal_code_format',
          'postal_code_regex','languages','neighbbours')
        self.writer.writerow(self.fields)
    
    def __call__(self,url,html):
        if re.search('/view/',url):
            tree=lxml.html.fromstring(html)
            row=[]
            for field in self.fields:
                row.append(tree.cssselect('table >tr#places_{}__row >td.w2p_fw'.format(field))[0].text_content())
            self.writer.writerow(row)
            
        
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