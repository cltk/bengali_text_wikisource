#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 09:35:51 2017

@author: djokester
Samriddhi Sinha
IIT Kharagpur 
"""

import requests
from bs4 import BeautifulSoup
import time

"""
getBengaliNum() converts arabic numbers to the Bengali Script. 
"""
def getBengaliNum(N):
    num_list = ["০", "১", "২", "৩", "৪", "৫", "৬", "৭", "৮", "৯"]
    N_list = list(str(int(N)))
    N_Beng = []
    for i in N_list:
        N_Beng.append(num_list[int(i)])
    N_Beng = "".join(N_Beng)    
    return(N_Beng)


bookName = "গীতাঞ্জলি" #Original name of the book. 
textFileNumber = 2
totalPages = 25

for i in range(0,10):
    url = "https://bn.wikisource.org/wiki/গীতাঞ্জলি/" + getBengaliNum(i)
    fileName = str(i)+".txt"
    r  =  requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,"lxml")
    stats = soup.find_all("span", {"class":"mw-poem-indented"})
    for stat in stats:
        data = stat.text + "\n"
        print(data)
        file = open(fileName,'a+')
        file.write(data)
        time.sleep(1)
        
    