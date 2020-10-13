from colorama import init, Fore, Back, Style
from bs4 import BeautifulSoup
import requests
import time
import os
import json

init()
website = "https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2"

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW,
          Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]


while True:
    try:
        print("REFRESHING ", end="")
        time.sleep(1)
        print("-> DOWNLOADING ", end="")
        time.sleep(1)
        page = requests.get(website)
        print("-> PARSING ", end="")
        time.sleep(1)
        soup = BeautifulSoup(page.text, "html.parser")
        print("-> FILTERING ", end="")
        os.system("cls")
        time.sleep(1)
        data = soup.find(id="registerData")
        data = data.text
        data = json.loads(data)
        print(data["description"])
        print()
        data = json.loads(data["parsedData"])
        namelength = 0
        countlength = 0
        deadlength = 0
        for dataline in data:
            if(len(str(dataline["Województwo"]))+2) > namelength:
                namelength = len(str(dataline["Województwo"]))+2
            if(len(str(dataline["Liczba"]))) > countlength:
                countlength = len(str(dataline["Liczba"]))
            if(len(str(dataline["Liczba zgonów"]))) > deadlength:
                deadlength = len(str(dataline["Liczba zgonów"]))
        for index, dataline in enumerate(data):
            print(colors[(index % len(colors))], "[", str(dataline["Województwo"]).title(), "]: ", " "*(namelength - len(str(dataline["Województwo"]))-2), "Liczba: ",
                  dataline["Liczba"], " "*(countlength - len(str(dataline["Liczba"]))), " Liczba zgonów: ", " "*(deadlength - len(str(dataline["Liczba zgonów"]))), dataline["Liczba zgonów"], sep="")
        time.sleep(60)
        print(Fore.RESET, end="")
    except Exception as e:
        print(e)
