# Meat of the scrape
'''
Go to each link and scrape the useful info

'''


base_dir="https://magic.wizards.com/"
base_url="https://magic.wizards.com/en/content/deck-lists-magic-online-products-game-info"

with open('linklist.csv', 'r') as f:
    reader = csv.reader(f)
    links_ls = list(reader)
del links_ls[0]
links = [item for sublist in links_ls for item in sublist]

def scrape(N,links):
    import requests 
    from bs4 import BeautifulSoup
    import pandas as pd
    import numpy as np
    import re
    import h5py
    from selenium import webdriver
    import time
    import json
    import csv
    Headers=['Play Type','Deck Name', 'Card Type','Card Count', 'Card Name', 'Card Link', \
             'Sideboard Card Count', 'Sideboard Card Name', 'Sideboard Link']
    deck_data_ls=[]
    deck_name_ls=[]
    for page in links[0:N-1]:
        page_url=base_dir+page
        r=requests.get(page_url)
        c=r.content
        page_soup=BeautifulSoup(c,"html.parser")
        Play_Type=page.split("/")[-1]

        for deckname in page_soup.find_all("div",{"class":"deck-group"}):
            deck_name=deckname.find("span",{"class":"deck-meta"}).h4.string
            deck_name_ls.append(deck_name)
            card_type=[]
            card_count=[]
            card_name=[]
            card_link=[]
            sideb_count=[]
            sideb_name=[]
            sideb_link=[]

            for card in deckname.find("div", {"class":"sorted-by-overview-container"}).find_all("div",{"class":"element"}):
                card_type.append(card.h5.text)
                card_count.append(card.find("span",{"class":"card-count"}).text)
                card_name.append(card.find("span",{"class":"card-name"}).text)
                try:
                    card_link.append(card.find("span",{"class":"card-name"}).a.get('href'))
                except AttributeError:
                    card_link.append(card.find('NaN'))

            try:    
                for sideb in deckname.find("div", {"class":"sorted-by-sideboard-container"}).find_all("span",{"class":"row"}):
                    sideb_count.append(sideb.find("span",{"class":"card-count"}).text)
                    sideb_name.append(sideb.find("span",{"class":"card-name"}).text)
            except AttributeError:
                sideb_count.append('NaN')
                sideb_name.append('NaN')

                try:
                    sideb_link.append(sideb.find("span",{"class":"card-name"}).a.get('href'))
                except AttributeError:
                    sideb_link.append('NaN')

            deck_data=dict(zip(Headers,[Play_Type,deck_name,card_type, card_count,\
                                 card_name, card_link, sideb_count, sideb_name, sideb_link])) 
            deck_data_ls.append(deck_data)
    return deck_data_ls
