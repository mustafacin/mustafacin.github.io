#!/usr/bin/python

import requests,argparse
try:
   ap = argparse.ArgumentParser()    
   ap.add_argument("-w", "--wordlist",required=True, help="sayi giriniz")
   ap.add_argument("-u", "--url", required=True, help="url giriniz")
   args = ap.parse_args()
except:
   print("\nExample : python fuzz.py -u http://10.10.10.185/ -w /usr/share/dirb/wordlists/common.txt\n")


args = ap.parse_args()
url=str(args.url)
dosya = open(args.wordlist,"r")
icerik=dosya.read()

for i in icerik.splitlines():
	if not i in str('#'):
           url_istek = url+str(i)
           sonuc = requests.get(url=url_istek)

           if str(200) in str(sonuc.status_code):
                print(i+"/  => 200 (OK) ") 

           elif str(301) in str(sonuc.status_code):
                print(i+"/ => 301 (Moved Permanently) ")

           elif str(204) in str(sonuc.status_code):
               print(i+"/ => 204 (No Content) ")

           elif str(302) in str(sonuc.status_code):
               print(i+"/ => 302 (Found) ")

           elif str(301) in str(sonuc.status_code):
               print(i+"/ => 307 (Temporary Redirect) ")

           elif str(401) in str(sonuc.status_code):
               print(i+"/ => 401 (Unauthorized) ")

           elif str(403) in str(sonuc.status_code):
               print(i+"/ => 403 (Forbidden) ")

