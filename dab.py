import sqlite3
import requests
from bs4 import BeautifulSoup

URL = 'https://result.unom.ac.in/results/ugresultpage.asp'
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'sec-ch-ua': '"Brave";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'x-requested-with': 'XMLHttpRequest',
    'Referrer-Policy': 'strict-origin-when-cross-origin'
}

data = {
    'regno':'312202661'
}
