
import time
from bs4 import BeautifulSoup
from urllib import request
from collections import Counter
import json, re
from timer.timer import Timer

"""
Målet med dette programmet er å få samlet de mest brukte titlene for annonser på Finn.no.
Dataen samlet inn bruker jeg deretter på å innsnevre søkebegrep for å kunne finne "gull"


"""

def loadPage(next=False,pagenum=1):
        if next == True:
            url = URL
            url+="&page={}".format(pagenum)
            html = request.urlopen(url)
        if html.status != 200:
            print("Nettverksfeil - Statuskode: %s, venter 10 sekunder" % html.status)
            time.sleep(10)
            html = request.urlopen(url)
            if html.status != 200: return False
            else: return html

        else:
            return html


def hentResultat(content):
    if content == False:
        print("Ingen innhold å gå gjennom. \nSjekk nettkoblingen eller URL'en.")
        return
    else:
        soup = BeautifulSoup(content,'html.parser')
        search_results = soup.find("script",attrs={'id':'__NEXT_DATA__'}).text
        listings : list = json.loads(search_results)['props']['pageProps']['search']['docs']
        return listings

def wordFrequency(wordlist):
    if type(wordlist) == str and len(wordlist) > 1:
        wordlist: list = re.findall(r'\w+',wordlist)
        popwords = Counter(wordlist).most_common(COUNTER_WORDS)
        return popwords
    elif type(wordlist) == str and len(wordlist) == 0:
        print("The list contains no words.")

    elif type(wordlist) == list and len(wordlist) > 0:
        pop_sentenes = Counter(wordlist).most_common(COUNTER_WORDS)
        return pop_sentenes
    elif type(wordlist) == list and len(wordlist) == 0:
        print("list contains no word.")

def enumSentences(listings):
    header_list :list =[]
    if not listings:
        print("enumSentences failed, no items to enumerate")
    else:
        for listing in listings:
            title = listing['heading'].lower()
            header_list.append(title)
        return header_list

def enumWords(listings):
    wordlist :str = ""
    if listings:
        for listing in listings:
            wordlist+=listing['heading'].lower()
        return wordlist

    else: print("something happened")

def enumPages():
    with Timer():
        listings :list = []
        for page in range(1,MAX_PAGES+1):
            if page % (DEBUG_INTERVAL) == 0:
                print("Laster inn side nr. %s" % page)
            html = loadPage(next =True,pagenum=page)
            if not html:
                print("Kunne ikke laste inn nettsiden. sjekk nettverktilkopling")
                return
            else:
                listings += hentResultat(html)
        if listings:
            return listings
        else: return False

def main():
  #  listings :list = hentResultat(loadPage())
    listings :list = enumPages()
    top_500_sentences = wordFrequency(enumSentences(listings))
    top_500_words = wordFrequency(enumWords(listings))
    return top_500_sentences,top_500_words


def flushToFile(*args):
    index = 0
    for arg in args:
        with open(DUMP_FILES[index],'w') as f:
            f.write('\n'.join('%s %s' % x for x in arg))
        index+= 1



if __name__ == '__main__':
    COUNTER_WORDS = 2500
    MAX_PAGES = 10
    DEBUG_INTERVAL = 10
    DUMP_FILES = "freq-sentences","freq-words"
    URL = 'https://www.finn.no/bap/forsale/search.html?q=NOT+%2265w+lader%22+NOT+adaptere+NOT+%22b%C3%A6rbar+stativ%22+NOT+bag+NOT+blekkpatron+NOT+blekkpatroner+NOT+brenner+NOT+%22data+cable%22+NOT+%22data+mus%22+NOT+datamus+NOT+dataveske+NOT+%22display+port%22+NOT+displayport+NOT+dvd+NOT+dvi-adapter+NOT+%22energizer+batteri%22+NOT+eske+NOT+etui+NOT+%22gaming+mus%22+NOT+gamingmus+NOT+%22hdmi+kabel%22+NOT+%22internett+kabel%22+NOT+ipad-cover+NOT+%22ipad+deksel%22+NOT+%22ipad+etui%22+NOT+kalkulator+NOT+kensington+NOT+kj%C3%B8leskap+NOT+lader+NOT+%22laptop+bag%22+NOT+%22laptop+batteri%22+NOT+magsafe+NOT+meter+NOT+%22microsoft+office%22+NOT+%22mini+holder%22+NOT+mouse+NOT+musematte+NOT+%22nettbrett+holder%22+NOT+nettbrettholder+NOT+nettverkskabel+NOT+%22patche+%22+NOT+pc-holder+NOT+%22pc+mappe%22+NOT+pc-mappe+NOT+pc-pute+NOT+%22pc+sekk%22+NOT+pc-sekk+NOT+%22pc+skjerm%22+NOT+%22pc+spill%22+NOT+%22pc+veske%22+NOT+printer+NOT+pute+NOT+reiseadapter+NOT+riser+NOT+%22s-ata+kabel%22+NOT+%22sata+kabel%22+NOT+skjermkabel+NOT+skj%C3%B8tekabel+NOT+skriver+NOT+skruer+NOT+sleeve+NOT+%22smart+cover%22+NOT+stativ+NOT+str%C3%B8madapter+NOT+str%C3%B8mkabel+NOT+%22tabler+holder%22+NOT+targus+NOT+tastatur+NOT+thinkpad-batteri+NOT+thunderbolt+NOT+toner+NOT+%22usb+kabel%22+NOT+%22usb+mus%22+NOT+v%C3%A6ske+NOT+veske+NOT+%22vga+adapter%22+NOT+%22vga+kabel%22+NOT+vifte+NOT+webcam+NOT+webkamera&sort=RELEVANCE&sub_category=1.93.3215&trade_type=1&trade_type=2'
    sentences,words = main()
    flushToFile(sentences, words)


    
    