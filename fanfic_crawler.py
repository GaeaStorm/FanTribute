#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import re
import pdfkit


# In[2]:


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    text = re.sub(cleanr, '', raw_html)
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text[5:]


# In[3]:


def utf_processing(text):
    text = text.replace("—", "-")
    text = text.replace("é", "e")
    return text


# In[4]:


def get_story(story_id):
    page_id = 1
    title = ""
    while (True):
        try:
            URL = 'https://www.fanfiction.net/s/' + str(story_id) + '/' + str(page_id)
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            if page_id == 1:
                title = cleanhtml(soup.find(id='profile_top').prettify())[6:]
                title = title[:title.find('\n')]
                pdfkit.from_string("", title + '.pdf')
                
            results = soup.find(id='storytext')
            pdfkit.from_string(utf_processing(results.prettify()), title + '.pdf')
        except Exception as e:
            print(e)
            break
        
        page_id+=1


# In[5]:


get_story(11575984)


# In[ ]:





# In[ ]:





# In[ ]:




