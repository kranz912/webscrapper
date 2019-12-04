from bs4 import BeautifulSoup
import httplib2
import urllib
import csv
import re

http = httplib2.Http()


def urltopdf(url,output):
    status, resp  = http.request(url)
    location = urllib.parse.urlparse(url).netloc

    soup = BeautifulSoup(resp, 'html.parser')
    

    paragraphs = soup.find_all(['p','h2','h4','h5','h3','li'])
    

    texts = []
    for paragraph in paragraphs:
        texts.append(paragraph)

    
    writeCSV(texts,output)

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


def writeCSV(list, output):
    with open(output,mode='w',encoding='utf-8') as c:

        for l in list:
            c.write(cleanhtml(str(l)))
            c.write('\n\n\n')
            
urltopdf('http://nitrongroup.com/about-us/','about-us.txt')

urltopdf('http://nitrongroup.com/our-products/','our-products.txt')
urltopdf('http://nitrongroup.com/where-we-are/','where-we-are.txt')
urltopdf('http://nitrongroup.com/csr/','csr.txt')

urltopdf('http://nitrongroup.com/contact-us/','contact-us.txt')