# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import urllib2
import re
import itertools

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
#
#max_errors=5
#num_errors=0
#for page in itertools.count(1):  
#    #itertools可以提供操作迭代器  count(1)可以生成无线迭代器 一直产生整数
#    url='http://example.webscraping.com/view/-%d' % page
#    html=download(url)
#    if html is None:
#        num_errors+=1
#        if num_errors==max_errors:
#            break
#    else :
#        num_errors=0

def link_crawler(seed_url,link_regex):
    crawl_queue=[seed_url]
    while crawl_queue:
        url=crawl_queue.pop()
        html=download(url)
        for link in get_links(html):
            if re.match(link_regex,link):
                crawl_queue.append(link)

def get_links(html):
    webpage_regex=re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    return webpage_regex.findall(html)

link_crawler('http://example.webscraping.com','/(index|view)')
crawl_sitemap('http://example.webscraping.com/sitemap.xml')