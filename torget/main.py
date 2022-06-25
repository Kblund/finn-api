import concurrent.futures
import threading
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
from collections import Counter
import json, re
from timer.timer import Timer

"""
Målet med dette programmet er å få samlet de mest brukte titlene for annonser på Finn.no.
Dataen samlet inn bruker jeg deretter på å innsnevre søkebegrep for å kunne finne "gull"
&sort=PRICE_ASC

"""

def loadPage(pagenum=1,allSortings=False):
    sortings = ["&sort=PRICE_ASC","&sort=RELEVANCE","&sort=PRICE_DESC","&sort=PUBLISHED_DESC","&sort=PUBLISDHED_ASC"]
    url = URL_PS4
    def getListings(sorting="&sort=PRICE_ASC"):
        
        url = URL_PS4 +sorting + "&page={}".format(pagenum)

        with urlopen(url) as res:
            if res.status == 200:
                return res.read()
            else: 
                print("Nettverksfeil - Statuskode: %s" % res.status)
                return False
    if allSortings == False:
        res = getListings(url)
        return res
    elif allSortings == True:
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            collected_results = []
            for result in executor.map(getListings,sortings):
                collected_results.append(result)
            return collected_results



def hentResultat(content):
    if content:
        bs = BeautifulSoup(content, "html.parser")
        search_results = bs.find("script",attrs={'id':'__NEXT_DATA__'}).text
        
        listings : list = json.loads(search_results)['props']['pageProps']['search']['docs']
        
        return listings
    else:
        pass

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
        with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
            futures = {executor.submit(loadPage,page,allSortings=False): page for page in range(1,MAX_PAGES+1)}
            for future in concurrent.futures.as_completed(futures):
                try:
                    html = future.result()
                    
                    if html:
                        if type(html) == list:
                        
                            with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor1:
                                
                                for futurez in executor1.map(hentResultat,html):
                                    listings+= futurez
                                
                        elif type(html) == bytes:
                            
                            listings+= hentResultat(html)
                                

                except:
                    print("Nopw")
            return listings

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
    MAX_PAGES = 50
    DEBUG_INTERVAL = 10
    DUMP_FILES = "freq-sentences","freq-words"

    URL_PS4 = 'https://www.finn.no/bap/forsale/search.html?q=ps4+OR+%22playstation+4%22+OR+%22play+station+4%22+OR+playstation4+OR+%22play+station4%22+OR+%22ps+4%22+OR+%22%28ps4%29%22NOT+%22ps+4+spill%22+NOT+%22diverse+ps4+spill%22+NOT+%22spill+til+ps+4%22+NOT+%22selger+ps4+spill%22+NOT+%22spill+red+dead%22+NOT+%22valhalla+spill+til+ps4%22+NOT+%222%2F3%2F4+spill%22+NOT+%22spill+etc%22+NOT+spill%3A+NOT+far+NOT+%22call+of+duty+modern%22+NOT+%22call+of+duty+black%22+NOT+%22call+of+duty+wwii%22+NOT+%22call+of+duty+vanguard%22+NOT+%22fifa+ps4%22+NOT+%22fifa+15+ps4%22+NOT+fifa-samling+NOT+%22fifa+21+til+%22+NOT+%22fifa+21+ps4%2Fps5%22+NOT+%22ps4+kontroller+%22+NOT+ps4-kontrollere+NOT+ps4-spill+NOT+%22ps4-+spill%22+NOT+%22%C3%B8nsker+%C3%A5+kj%C3%B8pe%22+NOT+%22nye+ps4-kontrollere%22+NOT+%22spill+til%22+NOT+ratt+NOT+%22sfuf+impact%22+NOT+%22scuf+impact%22+NOT+%22scuf+infiniti%22+NOT+%22scuf+vantage.%22+NOT+mikrofon+NOT+marvel+NOT+marvels+NOT+playstation-spill+NOT+%22ghost+of%22+NOT+%22ghost+recon%22+NOT+%22xbox+one%22+NOT+%22har+lyst+p%C3%A5%22+NOT+%22xbox+360%22+NOT+%22diverse+ps4+spill%22+NOT+%22diverse+spill+til%22+NOT+%22diverse+ps4+spill%22+NOT+%22diverse+spill%22+NOT+kit+NOT+skylanders+NOT+str%C3%B8mforsyning&sort=PRICE_ASC'
    URL_TECH = 'https://www.finn.no/bap/forsale/search.html?price_to=1500&q=NOT+%2265w+lader%22+NOT+adaptere+NOT+%22b%C3%A6rbar+stativ%22+NOT+bag+NOT+blekkpatron+NOT+blekkpatroner+NOT+brenner+NOT+%22data+cable%22+NOT+%22data+mus%22+NOT+datamus+NOT+dataveske+NOT+%22display+port%22+NOT+displayport+NOT+dvd+NOT+dvi-adapter+NOT+%22energizer+batteri%22+NOT+eske+NOT+etui+NOT+%22gaming+mus%22+NOT+gamingmus+NOT+%22hdmi+kabel%22+NOT+%22internett+kabel%22+NOT+ipad-cover+NOT+%22ipad+deksel%22+NOT+%22ipad+etui%22+NOT+kalkulator+NOT+kensington+NOT+kj%C3%B8leskap+NOT+lader+NOT+%22laptop+bag%22+NOT+%22laptop+batteri%22+NOT+magsafe+NOT+meter+NOT+%22microsoft+office%22+NOT+%22mini+holder%22+NOT+mouse+NOT+musematte+NOT+%22nettbrett+holder%22+NOT+nettbrettholder+NOT+nettverkskabel+NOT+%22patche+%22+NOT+pc-holder+NOT+%22pc+mappe%22+NOT+pc-mappe+NOT+pc-pute+NOT+%22pc+sekk%22+NOT+pc-sekk+NOT+%22pc+skjerm%22+NOT+%22pc+spill%22+NOT+%22pc+veske%22+NOT+printer+NOT+pute+NOT+reiseadapter+NOT+riser+NOT+%22s-ata+kabel%22+NOT+%22sata+kabel%22+NOT+skjermkabel+NOT+skj%C3%B8tekabel+NOT+skriver+NOT+skruer+NOT+sleeve+NOT+%22smart+cover%22+NOT+stativ+NOT+str%C3%B8madapter+NOT+str%C3%B8mkabel+NOT+%22tabler+holder%22+NOT+targus+NOT+tastatur+NOT+thinkpad-batteri+NOT+thunderbolt+NOT+toner+NOT+%22usb+kabel%22+NOT+%22usb+mus%22+NOT+v%C3%A6ske+NOT+veske+NOT+%22vga+adapter%22+NOT+%22vga+kabel%22+NOT+vifte+NOT+webcam+NOT+webkamera&sort=RELEVANCE&sub_category=1.93.3215&trade_type=1&trade_type=2'
    sentences, words = main()
    flushToFile(sentences, words)


    
    