#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 09:35:51 2017

@author: djokester
"""

import requests
from bs4 import BeautifulSoup
import time


bookName = "শকুন্তলা" #Original name of the book. 
textFileNumber = 2
segment_names = ["শকুন্তলা","দুষ্মন্ত", "তপোবনে", "রাজপুরে"]
count = 0
for segment in segment_names:
    count+=1
    url = "https://bn.wikisource.org/wiki/শকুন্তলা_(আদি_ব্রাহ্মসমাজ_সংস্করণ)/" + segment
    fileName = str(count)+".txt"
    r  =  requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,"lxml")
    stats = soup.find_all("p")
    for stat in stats:
        data = stat.text + "\n" 
        print(data)
        file = open(fileName,'a+')
        file.write(data)
        time.sleep(2)
        