#pylint:disable=W0401
from rubika.client import *
import rainbowtext, pyfiglet
from time import *
from numbers import *
import requests
import os
import datetime 
import time
import socket
import sys
from json import dumps,loads
yellow = "\033[93m"
green = "\033[32m"
red = "\033[31m"
blue = "\033[36m"
pink = "\033[35m"
white = "\033[00m"
# mark
w = str(datetime.datetime.now())
mark = '\x1b[38;5;4m' #blue
mark1 = '\x1b[48;5;15m' # blake for back ground
mark2 = '\x1b[0m' #end ..	
def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(0.09)
print(f"{green}")
print("--------------------------------")     	
seven=input(f'{red}[◐]{green}License -> ')
print("--------------------------------")
if seven =='monji024':
	print(f"""{yellow}[~] {red}That's right, friend""")
else:
		while True:
			print(f'{red}[~] error ')
		exit()
sprint(f'''{green}Welcome to the account control script''')
j = (f"""{white}
⣿⣿⣿⣿⣿⡿⠋⠁⠄⠄⠄⠈⠘⠩⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠻⣿⣿⣿⣿
⣿⣿⣿⣿⠄⠄⣀⣤⣤⣤⣄⡀⠄⠄⠄⠄⠙⣿⣿⣿
⣿⣿⣿⣿⡀⢰⣿⣿⣿⣿⣿⢿⠄⠄⠄⠄⠄⠹⢿⣿
⣿⣿⣿⣿⣿⡞⠻⠿⠟⠋⠉⠁⣤⡀⠄⠄⠄⠄⠄⠄
⣿⣿⣿⣿⣿⣿⣶⢼⣷⡤⣦⣿⠛⡰⢃⠄⠐⠄⠄⢸
⣿⣿⣿⣿⣿⣿⣿⡯⢍⠿⢾⡿⣸⣿⠰⠄⢀⠄⠄⡬
⣿⣿⣿⣿⣿⣿⣿⣴⣴⣅⣾⣿⣿⡧⠦⡶⠃⠄⠠⢴
⣿⣿⣿⣿⠿⠍⣿⣿⣿⣿⣿⣿⣿⢇⠟⠁⠄⠄⠄⠄
⠟⠛⠉⠄⠄⠄⡽⣿⣿⣿⣿⣿⣯⠏⠄⠄⠄⠄⠄⠄
⠄⠄⠄⢀⣾⣾⣿⣤⣯⣿⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄
{pink}Rubika ➫ @monji024

{red}I LOVE YOU💔

{mark1}{red}
『{w}』
{mark2}
""")
for n in j:
    sys.stdout.write(n)
    sys.stdout.flush()
    time.sleep(0.009)	
print(f"{green}")
print("--------------------------------")  
time.sleep(0.5)
z = input (f"{red}[~]{green}Installing the library -> <y/n> :")

if z == "y":
	os.system("pip install colorama && pip install rubika && pip install pyfiglet && pip install datetime && pip install rainbowtext && pip install requests")
print (f"{yellow}")
if z == "n":
    print()
    print("\r ok montaze bmon  ..",end="",flush=False)
    time.sleep(1)
    print("\r ok montaze bmon  ...",end="",flush=False)
    time.sleep(1)
    print("\r ok montaze bmon  ....",end="",flush=False)
    time.sleep(1)
    print("\r ok montaze bmon  .....",end="",flush=False)
    time.sleep(1)
    print("\r ok montaze bmon        ",end="",flush=False)
    time.sleep(0.8)
    print("\r ok montaze bmon  .",end="",flush=False)
    time.sleep(0.9)
    print("\r ok montaze bmon  .. ",end="",flush=False)
    time.sleep(0.5)
    print("\r ok montaze bmon  ...",end="",flush=False)
    time.sleep(0.7)
    print("\r ok montaze bmon  ....",end="",flush=False)
    time.sleep(1)
    print("\r ok montaze bmon  .....",end="",flush=False)
    time.sleep(0.7)
    print("\r ok montaze bmon           ",end="",flush=False)
print("")    
print("")    
print("--------------------------------")  
print(rainbowtext.text(pyfiglet.figlet_format('monji')))
p = input(f"{red}[~]{yellow}auth accuont ro vared kon ->")
bot = Bot("app_name",auth=p)
print("--------------------------------")  
d = input(f"{red}[~]{blue}guid accuont fard ro vared kon ->")
target =d
mo = input(f"{red}[~]{blue}guid makani ke mikhai paiam bdi ->")
target2 =mo
ko = input(f"{red}[~]{pink}Enter your message ->")
bot.sendMessage(target2,ko)
print("--------------------------------")  
m = input(f"{red}[~]{green}name change😈 ->")
bot.editProfile(first_name=m)
print("--------------------------------")  
h = input(f"{green}[~]{blue}bio change ->")
bot.editProfile(bio=h)
print("--------------------------------")  
q = input(f"{red}[~]{green}Change ID ->")
bot.editProfile(username=q)
print("--------------------------------")  
e = input(f"{red}[~]{yellow}Change profile ->")
bot.uploadAvatar(target,e)
print("--------------------------------")  
monji=input("{red}[~]{yellow}Throwing out of the account -> <y/n>")
if monji == "y":
	os.system("logout()")
if monji == "n":
	os.system("clear")
print('')
print("--------------------------------")  
print(f"{green}[+ ok⸽end]")
