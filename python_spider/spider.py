# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import urllib2
import re
import itertools
import urlparse
import robotparser


" 下载网页重试下载 "
def download(url,user_agent='wswp',proxy=None,num_retries=2):
    print 'downloading:',url
    headers={'User-agent':user_agent}
    request=urllib2.Request(url,headers=headers)
    
    opener=urllib2.Request(url,headers=headers)
    if proxy:
        proxy_params={urlparse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
        #支持代理 更友好的Python HTTP request
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
    seen=set(crawl_queue)
    rp=robotparser.RobotFileParser()
    rp.set_url(seed_url+'/robots.txt')
    rp.read()
    while crawl_queue:
        url=crawl_queue.pop()
        #if rp.can_fetch(): ？？？？？
            #检测指定用户代理是否允许访问网页
        html=download(url)
        for link in get_links(html):
            if re.match(link_regex,link):
                link=urlparse.urljoin(seed_url,link)
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)

def get_links(html):
    webpage_regex=re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    return webpage_regex.findall(html)

class Throttle:
    #对爬虫下载进行限速
    def __init__(self,delay):
        self.delay=delay
        self.domains={}
    def wait(self,url):
        domain=urlparse.urlparse(url).netloc
        last_accessed=self.domains.get(domain)
        
        if self.delay>0 and last_accessed is not None:
            sleep_secs=self.delay- (datetime.datetime.now()-
                last_accessed).seconds
            if sleep_secs>0:
                time.sleep(sleep_secs)
        self.domains(domain)=datetime.datetime.now()
                                    
link_crawler('http://example.webscraping.com','/(index|view)')
crawl_sitemap('http://example.webscraping.com/sitemap.xml')