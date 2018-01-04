# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import urllib2
import re

" 下载网页重试下载 "
def download(url,user_agent='wswp',num_retries=2):
    print 'downloading:',url
    headers={'User-agent':user_agent}
    request=urllib2.Request(url,headers=headers)
    try:
        html=urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'download error:', e.reason
        html=None
        if num_retries>0:
            if hasattr(e,'code') and 500<=e.code<600:
                #对于错误在500-600之间的代码进行重试下载
                return download(url,user_agent,num_retries-1)
    return html


def crawl_sitemap(url):
    #download the sitemap file
    sitemap=download(url)
    links=re.findall('<loc>(.*?)</loc>',sitemap)
    #提取sitemap链接
    for link in links:
        html=download(link)

crawl_sitemap('http://example.webscraping.com/sitemap.xml')