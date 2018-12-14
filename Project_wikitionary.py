import requests
from bs4 import BeautifulSoup

main_wiki = 'https://en.wiktionary.org/wiki/'

# Here the program starts:
""" This program takes input word from user and find its meaning
on wikitionary website and sends back result"""
print("----Your personal wikitionary dictionary---")
while True:
    word = input("Enter you Word: ")
    wiki = main_wiki + word
    res = requests.get(wiki)
    soup = BeautifulSoup(res.text, "lxml")
    noun = soup.find(id="Noun")
    adjective = soup.find(id="Adjective")
    verb = soup.find(id="Verb")
    
    if(noun or adjective or verb):
        print('\nYOUR WORD: ' + word.upper())
        print("===============Meanings==================")
        if(noun):
            print("NOUN")
            mean = noun.parent.find_next_sibling('ol').li
            while not mean.text:
                mean = noun.parent.find_next_sibling('ol').li.next_sibling
            print(mean.text.split('.')[0] + '.\n')
        if(adjective):
            print("ADJECTIVE")
            mean = adjective.parent.find_next_sibling('ol').li
            while not mean.text:
                mean = adjective.parent.find_next_sibling('ol').li.next_sibling
            print(mean.text.split('.')[0] + '.\n')
        if(verb):
            print("VERB")
            mean = verb.parent.find_next_sibling('ol').li
            while not mean.text:
                mean = verb.parent.find_next_sibling('ol').li.next_sibling
            print(mean.text.split('.')[0] + '.\n')
    else:
        print("Nothing")
    
    check = input("Translate another word: yes/no[Y/N]? ")
    if(check == 'no' or check == 'n' or check == 'N'):
        break

