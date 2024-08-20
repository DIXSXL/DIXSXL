import ipinfo

import pystyle

import subprocess as sb

from colorama import init, Fore

from pystyle import Colors



try:

	import ipinfo

except:

	os.system('pip install ipinfo')

	import ipinfo



ip = input(pystyle.Colorate.Horizontal(Colors.blue_to_white, "введите IP: "))

access_token = "cda874226c0c24"



try:

	handler = ipinfo.getHandler(access_token)

	details = handler.getDetails(ip)

except:

	print(Fore.RED + "ошибка")





try:

	print(pystyle.Colorate.Horizontal(Colors.blue_to_white, f"""

		IP INFO



		  IP > {details.ip} 

		  HOSTNAME > {details.hostname} 

		  CITY > {details.city} 

		  REGION > {details.region} 

		  COUNTRY > {details.country} 

		  LOC > {details.loc} 

		  ORG > {details.org} 

		  TIMEZONE > {details.timezone} 

		"""))

except:

	print(Fore.RED + "ошибка")







def on_request_uri():

	url = 'https://ip2geolocation.com/?ip=' + str(ip)

	print('>>> ссылка на отчет >>> ' + str(url))



on_request_uri()
