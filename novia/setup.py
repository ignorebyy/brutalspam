import requests, random, json, sys, base64
from fake_useragent import UserAgent

a= '\033[1;30m'; m = '\033[1;31m';h = '\033[1;32m'; p= '\033[1;37m'; k = '\033[1;33m'
ua = UserAgent().random
rp = requests.post
jd = json.dumps



kont = requests.post('http://lerr.42web.io/remote.html?i=1')
if "Running" in kont.text:
	status = f'{h} Online '
else:
	status = f'{p} Offline '

logo = f'''
{m} ____ {p} ____   __   _  _  _  _  ____  ____ {m}          __  ____
{m}/ ___){p}(  _ \ / _\ ( \/ )( \/ )(  __)(  _ \{a}   ___ {m}  (  )(    \\
{m}\___ \{p} ) __//    \/ \/ \/ \/ \ ) _)  )   /{a}  (___){m}   )(  ) D (
{m}(____/{p}(__)  \_/\_/\_)(_/\_)(_/(____)(__\_){m}         (__)(____/{p} v2

 {m}[{p} /{m} ]{p} Author :{k} IpanCryzz{status}
 {m}[{p} /{m} ]{p} Github :{a} https://github.com/twincry/spammer
'''
