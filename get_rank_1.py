#!/usr/bin/env python3
"""
This Module contains functions that get the url of the top /r/programming post
"""
import bs4
import requests


def get_rank_test():
    res = requests.get("https://www.reddit.com/r/programming/")
    res.raise_for_status()
    programming_pg_soup = bs4.BeautifulSoup(res.text, "html5lib")
    for link in programming_pg_soup.find_all('div'):
        print(link.attrs)
        print('\n\n\n')
        if link.get('data-rank') == '1':
            return(link.get('data-url'))

"""
Gets the title and post 1 of /r/programming
"""
def get_rank_1():
    res = requests.get("https://www.reddit.com/r/programming/")
    res.raise_for_status()
    programming_pg_soup = bs4.BeautifulSoup(res.text, "html5lib")
    link =  programming_pg_soup.find_all('div', {"data-rank" : "1"})
    link = link[0]
    a_tags = link.find_all('a')
    a_tags = a_tags[0]
    tweet = a_tags.contents[0] + ' : ' + link.get('data-url')
    return (tweet)
