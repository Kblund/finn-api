searchparam_tech = 'NOT "65w lader" NOT adaptere NOT "bærbar stativ" NOT bag NOT blekkpatron NOT blekkpatroner NOT brenner NOT "data cable" NOT "data mus" NOT datamus NOT dataveske NOT "display port" NOT displayport NOT dvd NOT dvi-adapter NOT "energizer batteri" NOT eske NOT etui NOT "gaming mus" NOT gamingmus NOT "hdmi kabel" NOT "internett kabel" NOT ipad-cover NOT "ipad deksel" NOT "ipad etui" NOT kalkulator NOT kensington NOT kjøleskap NOT lader NOT "laptop bag" NOT "laptop batteri" NOT magsafe NOT meter NOT "microsoft office" NOT "mini holder" NOT mouse NOT musematte NOT "nettbrett holder" NOT nettbrettholder NOT nettverkskabel NOT "patche " NOT pc-holder NOT "pc mappe" NOT pc-mappe NOT pc-pute NOT "pc sekk" NOT pc-sekk NOT "pc skjerm" NOT "pc spill" NOT "pc veske" NOT printer NOT pute NOT reiseadapter NOT riser NOT "s-ata kabel" NOT "sata kabel" NOT skjermkabel NOT skjøtekabel NOT skriver NOT skruer NOT sleeve NOT "smart cover" NOT stativ NOT strømadapter NOT strømkabel NOT "tabler holder" NOT targus NOT tastatur NOT thinkpad-batteri NOT thunderbolt NOT toner NOT "usb kabel" NOT "usb mus" NOT væske NOT veske NOT "vga adapter" NOT "vga kabel" NOT vifte NOT webcam NOT webkamera '
searchparam_ps4 = 'ps4 OR "playstation 4" OR "play station 4" OR playstation4 OR "play station4" OR "ps 4" OR "(ps4)"NOT "ps 4 spill" NOT "diverse ps4 spill" NOT "spill til ps 4" NOT "selger ps4 spill" NOT "spill red dead" NOT "valhalla spill til ps4" NOT "2/3/4 spill" NOT "spill etc" NOT spill: NOT far NOT "call of duty modern" NOT "call of duty black" NOT "call of duty wwii" NOT "call of duty vanguard" NOT "fifa ps4" NOT "fifa 15 ps4" NOT fifa-samling NOT "fifa 21 til " NOT "fifa 21 ps4/ps5" NOT "ps4 kontroller " NOT ps4-kontrollere NOT ps4-spill NOT "ps4- spill" NOT "ønsker å kjøpe" NOT "nye ps4-kontrollere" NOT "spill til" NOT ratt NOT "sfuf impact" NOT "scuf impact" NOT "scuf infiniti" NOT "scuf vantage." NOT mikrofon NOT marvel NOT marvels NOT playstation-spill NOT "ghost of" NOT "ghost recon" NOT "xbox one" NOT "har lyst på" NOT "xbox 360" NOT "diverse ps4 spill" NOT "diverse spill til" NOT "diverse ps4 spill" NOT "diverse spill" NOT kit NOT skylanders NOT strømforsyning'
newparams :list = []

while True:
    user = input()
    if user != "--stop":
        if user.find(" ") > 0:
            user = '"' + user + '"'

        newparams.append(user)
    elif user == "--stop":
        break

hey = searchparam_ps4+ " ".join("NOT %s" % x for x in newparams)
print(hey)