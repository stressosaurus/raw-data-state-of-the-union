### SOTU: Website data wrangling Tools
## Alex John Quijano
## Created: 4/6/2019

from bs4 import BeautifulSoup
import os
import urllib.request
import numpy as np
import pandas as pd
import itertools
from tqdm import tqdm

def download_sotu(url):
    directory_html = 'html_files/'
    try:
    	os.makedirs(directory_html)
    except FileExistsError:
    	pass
    try:
        urllib.request.urlretrieve(url,directory_html+'sotu_table.html')
    except:
        print('Error: URL does not exist!')
    raw_html = open(directory_html+'sotu_table.html',encoding='utf-8').read()
    html = BeautifulSoup(raw_html, 'html.parser')
    table_html = html.select('table')
    links = {}
    print('Collecting urls from '+url+'...')
    for i in tqdm(table_html):
        rows = i.findAll('tr')
        for tr in rows:
            cols = tr.findAll('td')
            for td in cols:
                a = td.find('a')
                if a != None:
                    link_string = a.get('href')
                    if link_string != None:
                        try:
                            tester = links[a.text]
                        except:
                            links[a.text] = []
                        try:
                            links[a.text].append(link_string)
                        except:
                            pass
    label_all = []
    print('Downloading urls ...')
    for k in tqdm(links.keys()):
        links_k = links[k]
        links_k = np.unique(links_k)
        labels_k = []
        for j in range(0,len(links_k)):
            try:
                labels_k.append(k+'-'+str(j))
                urllib.request.urlretrieve(links[k][j],directory_html+k+'-'+str(j)+'.html')
            except:
                pass
        label_all.extend(labels_k)
    year = []
    month = []
    day = []
    president = []
    sotu_title = []
    sotu = []
    print('Processing urls ...')
    for i in tqdm(label_all):
        try:
            raw_html_page = open(directory_html+i+'.html',encoding='utf-8').read()
            html = BeautifulSoup(raw_html_page, 'html.parser')
            divs = html.select('div')
            for i in divs:
                div_class = i.get('class')
                if div_class != None:
                    # YR-MT-DY
                    if div_class[0] == 'field-docs-start-date-time':
                        span = i.select('span')
                        time_text = span[0].text
                        time_text = time_text.replace(',','')
                        time_text = time_text.split(' ')
                        year.append(time_text[2])
                        month.append(time_text[0])
                        day.append(time_text[1])
                    # PR
                    if div_class[0] == 'field-title':
                        h3 = i.select('h3')
                        a = h3[0].select('a')
                        president.append(a[0].text)
                    # TLT
                    if div_class[0] == 'field-ds-doc-title':
                        h1 = i.select('h1')
                        sotu_title.append(h1[0].text)
                    # SOTU
                    if div_class[0] == 'field-docs-content':
                        paragraphs = i.select('p')
                        paragraphs_all = []
                        for p in paragraphs:
                            paragraphs_all.append(p.text.replace('\t',' ').replace('\n',' '))
                        sotu.append(' '.join(paragraphs_all))
        except:
            pass

    month_code = {'January':1,'February':2,'March':3,
                  'April':4,'May':5,'June':6,'July':7,
                  'August':8,'September':9,'October':10,
                  'November':11,'December':12}

    table = {}
    table['year'] = [int(i) for i in year]
    table['month'] = [int(month_code[i]) for i in month]
    table['day'] = [int(i) for i in day]
    table['president'] = president
    table['title'] = sotu_title
    table['text'] = sotu
    table = pd.DataFrame(table).sort_values(by=['year','month','day'],ascending=False)

    return table
