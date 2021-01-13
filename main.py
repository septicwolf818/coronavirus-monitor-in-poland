"""Coronavirus monitor in Poland"""

from bs4 import BeautifulSoup
import prettytable
import requests
import time
import os
import platform
import json

website = "https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2"
system = platform.system()
if system == "Windows":
    clear = "cls"
elif system in ["Darwin", "Linux"]:
    clear = "clear"

os.system(clear)

while True:
    data = [line.split(";") for line in json.loads(BeautifulSoup(requests.get(
        website).text, "html.parser").find(id="registerData").text)["data"].split("\r\n")]

    table = prettytable.PrettyTable()

    table.field_names = data[0][:-1]

    for index, data_chunk in enumerate(data[1:-1]):
        table.add_row(data_chunk[:-1])

    print(table)
    time.sleep(60)
    os.system(clear)
