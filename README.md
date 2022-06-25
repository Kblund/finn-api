# finn-api
A Collection of Python-Scripts intended to automate and improve upon Finn.no's search engine

## Reise

This script scrapes every trip on Finn.no/reise, filtering them out by country and price.
Outputs an easily digestible text file with all needed relevant info.
Example below

```

Hotel Heleni Beach-Rhodos,Hellas 3-Stjerners
Fasiliteter:['balcony', 'pool', 'elevator', 'internet_available'] no_meals Avstand fra strand/by: None/None
Flyplass: OSL | 4543kr per pers.
Reisedato: 13-07-2022
Antall dager: 7
Link: https://www.ticket.no/deeplink.html?searchType=PACKAGE&returnTrip=true&isDestinationSearch=false&channel=PACKAGE&startDate=2022-07-13&outStartLocation=91fe6790-9b38-4dfa-a403-0a59729fbacb&endDate=2022-07-19&homeStartLocation=d50826a5-bd86-4586-9561-06afc2cf40a1&numberOfAdults=2&numberOfChildren=0&numberOfInfants=0&numberOfRooms=1&specificHotel=d477c99b-1c4f-4bfc-ae46-7084e6d09c22&source=finn&metaData=3b2a9f2504df7c30788a9e42e00fad6f91292697f4d9ebe2e08c7b11e78971c81dc27d65e2e6bfb523e7e9507756d42c&directFlight=false&flightSuppliers=GENERIC_SUNHOTELS,GENERIC_SEMBO,GENERIC_AMADEUS,GENERIC_EXPEDIA&airlineCodes=&cid=ano.bpaket.c2014-07.dr.efinn.fcpo.gxml.h1.ir.jtp

Marine Congo Hotel-Rhodos,Hellas 2-Stjerners
Fasiliteter:['balcony', 'pool', 'elevator', 'internet_available'] no_meals Avstand fra strand/by: 150/500
Flyplass: OSL | 4687kr per pers.
Reisedato: 13-07-2022
Antall dager: 7
Link: https://www.ticket.no/deeplink.html?searchType=PACKAGE&returnTrip=true&isDestinationSearch=false&channel=PACKAGE&startDate=2022-07-13&outStartLocation=91fe6790-9b38-4dfa-a403-0a59729fbacb&endDate=2022-07-19&homeStartLocation=d50826a5-bd86-4586-9561-06afc2cf40a1&numberOfAdults=2&numberOfChildren=0&numberOfInfants=0&numberOfRooms=1&specificHotel=1f55474b-1ab7-4ed1-807a-e27b6cc42c5d&source=finn&metaData=5c89b9820393deaf51a7dab6c5f11c845c051a0c1bdea064593c634464a3bc276aa5912b1026c6ebca9bc4f1c3299bf5&directFlight=false&flightSuppliers=GENERIC_SUNHOTELS,GENERIC_SEMBO,GENERIC_AMADEUS,GENERIC_EXPEDIA&airlineCodes=&cid=ano.bpaket.c2014-07.dr.efinn.fcpo.gxml.h1.ir.jtp

Marianna Apartments-Kos,Hellas 3-Stjerners
Fasiliteter:['balcony', 'pool', 'aircondition_available', 'internet_available'] no_meals Avstand fra strand/by: 900/0
Flyplass: OSL | 4708kr per pers.
Reisedato: 24-07-2022
Antall dager: 8
Link: https://www.ticket.no/deeplink.html?searchType=PACKAGE&returnTrip=true&isDestinationSearch=false&channel=PACKAGE&startDate=2022-07-24&outStartLocation=91fe6790-9b38-4dfa-a403-0a59729fbacb&endDate=2022-07-31&homeStartLocation=c54c211e-88dc-44c2-a428-d7c059a036e7&numberOfAdults=2&numberOfChildren=0&numberOfInfants=0&numberOfRooms=1&specificHotel=a75fec3d-bdfb-4531-891a-1663a10970ca&source=finn&metaData=1b680a0a9a9db3f3d002a8ff39caf1f6aaf8adb233a68b4fd0515827da66f982f01a3905a486ce52259b8f075403309c&directFlight=false&flightSuppliers=GENERIC_SUNHOTELS,GENERIC_SEMBO,GENERIC_AMADEUS,GENERIC_EXPEDIA&airlineCodes=&cid=ano.bpaket.c2014-07.dr.efinn.fcpo.gxml.h1.ir.jtp

Miranda Hostal-Costa Brava og Barcelona,Spania 2-Stjerners
Fasiliteter:['internet_available', 'restaurant'] no_meals Avstand fra strand/by: 200/200
Flyplass: OSL | 4918kr per pers.
Reisedato: 12-07-2022
Antall dager: 7
Link: https://www.solfaktor.no/search?hotelid=33041&id=43786&place=Blanes&airport=OSL&departure=2022-07-12&return=2022-07-18&rooms=1&room0adults=2&cs1=MjA1MC0xMi0xMjs3NjQ0NTk7Uk87MTs5ODM2OzsyOztPU0w7MTIvNzs2&scroll=search-results&meta=finn

Rena Apartments by Checkin-Kreta,Hellas 3-Stjerners
Fasiliteter:['balcony', 'restaurant', 'internet_available'] no_meals Avstand fra strand/by: None/None
Flyplass: OSL | 4928kr per pers.
Reisedato: 23-07-2022
Antall dager: 9
Link: https://www.ticket.no/deeplink.html?searchType=PACKAGE&returnTrip=true&isDestinationSearch=false&channel=PACKAGE&startDate=2022-07-23&outStartLocation=91fe6790-9b38-4dfa-a403-0a59729fbacb&endDate=2022-07-31&homeStartLocation=4e5615b9-5f53-40f3-885b-dd98caa916db&numberOfAdults=2&numberOfChildren=0&numberOfInfants=0&numberOfRooms=1&specificHotel=e79b0171-ed71-43fc-8218-c5834f3813ba&source=finn&metaData=c207b3fb18f878a5d1d0a1eeccf98fc285cb372703986b1f057fa19bb3dd2e5e9c9a0ea1da2a43b7eff797c8fbf79659&directFlight=true&flightSuppliers=GENERIC_SUNHOTELS,GENERIC_SEMBO,GENERIC_SIGNATOURS,GENERIC_AMADEUS,GENERIC_EXPEDIA&airlineCodes=&cid=ano.bpaket.c2014-07.dr.efinn.fcpo.gxml.h1.ir.jtp

```
## Torget

This script is meant to improve upon the search engine by using Finn.no's logical operators.
The result is a much more prescise search.
