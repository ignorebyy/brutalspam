from novia import setup as YANTO
from novia import sms, wa
import os, sys, time

def main():
	os.system('clear'); print(f'{YANTO.logo}')
	no = input(f'{YANTO.m} [{YANTO.p} + {YANTO.m}]{YANTO.p} Nomor Target :{YANTO.k} ')
	if len(no) < 10:
		print(f'{YANTO.m} [{YANTO.p} !{YANTO.m} ]{YANTO.p} Contoh{YANTO.a} 8xxxxxxxxxx{YANTO.p} Tanpa{YANTO.m} +62/0/62 '); time.sleep(3); os.system('python run.py')
	elif len(no) > 11:
		print(f'{YANTO.m} [{YANTO.p} !{YANTO.m} ]{YANTO.p} Contoh{YANTO.a} 8xxxxxxxxxx{YANTO.p} Tanpa{YANTO.m} +62/0/62 '); time.sleep(3); os.system('python run.py')
	else:
		print(YANTO.p+'-'*64); print(YANTO.p+'-'*64)
		try:
			while True:
				wa.eci(no); wa.bukwa(no); wa.sayur(no); wa.carsome(no); wa.vp(no); sms.mapclub(no); sms.momotor(no); sms.momobil(no); sms.rupa(no); sms.eci(no); sms.kdok(no); sms.lumma(no); sms.qoala(no); sms.redbus(no); sms.sayurbox(no)
		except:
			exit(f'{YANTO.m} [{YANTO.p} !{YANTO.m} ]{YANTO.p} Connection Aborted Error...')




if __name__=='__main__':
	if "Open" in YANTO.kont.text:
		main()
	else:
		print(f'{YANTO.m} [{YANTO.p} !{YANTO.m} ]{YANTO.p} Content Locked by Admin...')
