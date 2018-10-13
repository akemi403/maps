#!/usr/bin/env python3
#author : AKEMI403
#ieu teh jang neangan alamat

import os
import json,requests

class kolor():
	pink = '\033[95m'
	blue = '\033[94m'
	green = '\033[92m'
	yellow = '\033[93m'
	red = '\033[91m'
	end = '\033[0m'
	white = '\033[1m'
	under = '\033[4m'

os.system("clear")

print(kolor.yellow+"""
  _____ ___ _   _ ____  __  __    _    ____  ____  
 |  ___|_ _| \ | |  _ \|  \/  |  / \  |  _ \/ ___| 
 | |_   | ||  \| | | | | |\/| | / _ \ | |_) \___ \ 
 |  _|  | || |\  | |_| | |  | |/ ___ \|  __/ ___) |
 |_|   |___|_| \_|____/|_|  |_/_/   \_\_|   |____/ 

 NB : Kalian Bisa Mencari Alamat Menggunakan Kode Pos,
 Kelurahan, Kecamatan, Nama Jalan, Nama Tempat asalkan jangan
 kode bokep.. 
=======================================================""")
alamat = str(input(" Masukan Alamat : "))

if len(alamat) == 0:
	print(" Alamatnya Mana Pukimak")
	exit()
 
r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address={}&key=AIzaSyA1MgLuZuyqR_OGY3ob3M52N46TDBRI_9k".format(alamat))	
json = json.loads(r.text)

if json['status'] == "ZERO_RESULTS":
	print(" Maaf alamat yang anda cari tidak ada")
else:
	print("=======================================================")
	for i in json['results']:
		for oce in i['address_components']:
			print("",oce['long_name']," >> Types :",oce['types'][0])
		print("=======================================================")
		for i in json['results']:
			print(" Address : "+i['formatted_address'])
		print("=======================================================")
		print(" TITIK KORDINAT")
		for i in json['results']:
			print(str(" Latitude :"),i['geometry']['location']['lat'])
			print(str(" Longitude :"),i['geometry']['location']['lng'])
		print("=======================================================")



