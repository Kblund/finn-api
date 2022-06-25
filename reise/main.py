from datetime import datetime
import json
from os import path, getcwd
from urllib import parse, request
url = r'https://www.finn.no/reise/pakkereiser/api//offerService;sort=price;'

# https://www.finn.no/reise/pakkereiser/api//offerService;duration=5-15;
# to=%5B
#   %22Asia%3BThailand%3BPhuketomr%C3%A5det%3BKata%20Noi%20Beach%22
#   %2C%22Asia%3BThailand%3BPhuketomr%C3%A5det
# %3BNai%20Harn%20Beach%22%2C%22Asia%3BThailand%3BSentrale%20Thailand%22%2C%22Europa%3BHellas%3BTilos%22%2C%22Amerika%3BMexico%3BRiviera%20Maya%22%2C%22Amerika%3B
# Nederlandske%20Antiller%3BCuracao%20-%20Willemstad%22%2C%22Amerika%3BDominikanske%20republikk%22%5D;
# travelMonths=%5B%226.2022%22%5D
                # %20 = " "
                # %22 = " 
                # %5B = [ 
                # %5D = ] 
                # %3B = ; 
                # %2C = ,
            # ["to="Asia;Thailand;Phuketområdet","Europa;Hellas;Tilos"]
class FinnReiseURL():
    sort = ['price','best']
    url = 'https://www.finn.no/reise/pakkereiser/api//offerService;'

    def __init__(self,duration = None, travelDate = None,planeFrom = None,exclude = None):
        self.destinations = None;self.page = None;self.planeFrom = planeFrom
        self.exclude = exclude;self.duration = duration;self.travelDate = travelDate
        self.current_dir = None
        self.encodedUrl = None
        
        
    def createURL(self,destinations=None):
        exclusionList = [x.lower() for x in self.exclude]
        if self.planeFrom or self.destinations or self.travelDate or self.duration == None:
            self.prompt()
        fra,til,reisedato,varighet = None, None, None, None
        if self.exclude == None:
            self.exclude = ""
        if self.planeFrom =="":
            fra =''
        else: fra = "from=%s;" % self.planeFrom
        if destinations == "" or destinations == None:
            til = ('to=%5B')
            for v in self.destinations["plain"]:
                    if not any(cntry in v.lower() for cntry in exclusionList):
                         til +=parse.quote('"' +v + '",')
            temp = list(til)
            til = "".join(temp[0:-3])
            til += parse.quote(']')
        travelDate = parse.quote("travelMonths=[\""+ self.travelDate + "\"];",";=").format(self.travelDate)
        varighet = "duration=%s;" % self.duration
        urlstring = fra + travelDate + varighet + til
        self.encodedUrl = url + urlstring
        return self.encodedUrl

    def prompt(self):
        if self.planeFrom == None or self.planeFrom == "":
            self.planeFrom = input("Please enter your departure place: ") 
        if self.travelDate == None or self.travelDate == "":
            self.travelDate = input("Please enter your travel date: ") 
        if self.duration == None or self.duration == "":
            self.duration = input("Please enter your duration: ") 
        if self.travelDate == "":
            self.travelDate = "07.2022" 
        if self.duration == "":
            self.duration = "7-9"
       # self.exclude = input("Please enter places to exclude: ")
        return
    
    def Exists(self):
        lib = "lib"
        if "self.current_dir" not in vars():
            self.getCurrentPath()
        configFile = path.join(self.current_dir,lib)
        if not path.exists(configFile):
            print ("Directory %s does not exist" % configFile)
            return False
        return configFile
    
    def getCurrentPath(self):
        self.current_dir = path.dirname(__file__)
    def getDocument(self):
        configFile = self.Exists()
        if not configFile:
            print("No document found.")
        else:
            self.destinations = {}
            with open(path.join(configFile,"liste.txt"), 'r') as configFile:
                country = {}
                continent = {}
                city = []
                self.destinations["plain"] = []
                for x in configFile:
                    
                    line = x.replace("_", " ").strip().replace("Ã¸","ø").replace("Ã¥","å").replace("Ã˜","Ø")
                    self.destinations["plain"].append(line)
                    line=line.split(";")
                    print(line)
                    if len(line) > 2:
                       
                        city.append(line[2:])
                        country[line[1]] = city
                        continent[line[0]] = country
                    elif len(line) == 2:
                        
                        country[line[1]] = line[1]
                        continent[line[0]] = country
                        
                        
                    else: print("what")
                self.destinations.update(continent)

    def main(self,duration = "7-14",travelDate = "07.2022",
                     exclude = [
                         "Polen",
                         "Norge",
                         "Storbritannia",
                         "Estland",
                         "Østerrike",
                         "Danmark",
                         "Litauen",
                         "Ukraina",
                         "Serbia",
                         "Albania",
                         "Irland",
                         "Ungarn",
                         
                         "Tyskland",
                         "Latvia",
                         "Tsjekkia",
                         "Sverige",
                         "Italia"
                         ]):
        self.duration = duration; self.travelDate = travelDate; self.exclude = exclude
        self.getDocument()
        return self.createURL()
        
        
class FinnReise:
    
    def __init__(self,url=None,maxPrice=6000,maxPages=200):
        self.url :str = url
        self.currentPage :int = None
        self.totalPages :int = None
        self.offers : list = []
        self.filteredOffers : list = []
        self.maxPages = maxPages
        self.textualEntry = None
        self.maxPrice = maxPrice
        
    def hentSide(self,url):
        with request.urlopen(url) as req:
            if req.status == 200:
                responseData = json.loads(req.read())["data"]
                self.currentPage = responseData["currentPage"]
                self.totalPages = responseData["totalPages"]
                for offer in responseData["offers"]:
                    self.offers.append(offer)
                    
    def getPath(self,filtered=False):
        if filtered:
            dictPath = path.join(path.dirname(__file__),"lib","filtereddict.json")
            print("filterr")
        else:
            dictPath = path.join(path.dirname(__file__),"lib","dict.json")
        return dictPath
    
    def dumpToFile(self,filtered = False):
        if filtered:
            dictPath = self.getPath(filtered=True)
            offers = self.filteredOffers
            with open(dictPath,"w") as f:
                json.dump(self.filteredOffers,f)
        else:        
            dictPath = self.getPath()
            with open(dictPath,"w") as f:
                json.dump(self.offers,f)
                
    def iterHentSide(self):
        for page in range(1,self.maxPages +1):
            url = self.url + ";" + "page=%s" % page
            self.hentSide(url)
            
    def readFile(self,filtered = False):
        if filtered:
            dictPath = self.getPath(filtered = True)
            with open(dictPath,"r") as f:
                self.filteredOffers = json.load(f)      
        else: 
            dictPath = self.getPath()
            with open(dictPath,"r") as f:
                self.offers = json.load(f)

            
    def filterData(self):
        maxPrice = self.maxPrice
        minDate = datetime.strptime("2022-07-09T06:40","%Y-%m-%dT%H:%M")
        maxDate = datetime.strptime("2022-07-25T06:40","%Y-%m-%dT%H:%M")
        offers = []
        for offer in self.offers:
            offerDate = datetime.strptime(offer["departureDate"], "%Y-%m-%dT%H:%M")
            if offerDate > maxDate or offerDate < minDate:
                pass
            elif maxPrice < int(offer["pricePerPerson"]):
                pass
            else: 
                offers.append(offer)
        print("DONE",len(offers))
        self.filteredOffers = offers
    def generateText(self):
        self.textualEntry = []
        for k in self.filteredOffers:
            entry =[
                "\n"+k["hotelName"],"-",k["region"].strip() + ",", k["country"],  " " , str(k["rating"]) +"-Stjerners\n",\
                "Fasiliteter:",(k["facilities"])," " , k["board"]," Avstand fra strand/by: ", k["distanceToBeach"],"/",k["distanceToCity"],\
                "\nFlyplass: ",str(k["originAirportCode"])+" | "+ str(k["pricePerPerson"])+"kr per pers.\n" ,\
                "Reisedato: "+datetime.strftime(datetime.strptime(k["departureDate"],"%Y-%m-%dT%H:%M"),"%d-%m-%Y") ,"\nAntall dager: " , k["duration"],\
                "\nLink: "+k["deepLink"]]
            self.textualEntry.append(entry)
            
    def updateLocals(self):
        urlConstruct = FinnReiseURL()
        url = urlConstruct.main()
        self.url = url
        self.iterHentSide()
        self.dumpToFile()
        self.filterData()
        self.dumpToFile(True)
    def dumpText(self):
        if self.textualEntry:
            file = path.join(path.dirname(__file__),"lib","text.txt")
            with open(file,"w") as f:
                for entry in self.textualEntry:
                    y = "".join(str(x) for x in entry)
                    f.write(str(y))
                    f.write("\n")
                    
                
if __name__ == '__main__':
    """
    getURL = FinnReiseURL()
    url = getURL.main()
    print(getURL.destinations["Europa"].keys())
    print(url)
    
    """
    data = FinnReise()
 #   data.readFile(filtered = True)
    data.updateLocals()
  #  print(data.filteredOffers[0].keys())
    data.generateText()
    data.dumpText()

    #print(data.textualEntry[0])
#   data.dumpToFile(filtered=True)
