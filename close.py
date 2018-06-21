import requests
import json

import time
import threading
from datetime import datetime
import logging



logging.basicConfig(level=logging.INFO,
                format='%(asctime)s, %(levelname)s, %(message)s',
                datefmt='%d, %b, %H:%M:%S',
                filename='/storage/emulated/0/0/myapp.csv',
                filemode='a')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s: %(levelname)-s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def log(level,type, info):
    if(level==0):
        logging.debug(type+','+info)
    else:
        if(level== 1):
            logging.info(type+','+info)
        else:
            if(level ==2):
                logging.warning(type+','+info)
               

pa={'action':'get','v':'1500288514773'}
header={\
'Host':'wechat.ifanscloud.com',\
'Connection':'keep-alive',\
'Accept':'text/html, */*; q=0.01',\
'Origin':'http://wechat.ifanscloud.com',\
'X-Requested-With':'XMLHttpRequest',\
'User-Agent':'Mozilla/5.0 (Linux; Android 6.0.1; 1605-A01 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN',\
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',\
'Referer':'http://wechat.ifanscloud.com/Wechatwujia/app/2336/index.php?&openid=oKvvajr2WacI-GN7tGzsNjnZGpds',\
'Accept-Encoding':'gzip, deflate',\
'Accept-Language': 'zh-CN,en-US;q=0.8'\
, 'Content-Length': '100'}
C={'PHPSESSID':'t9c80vs5lon9r5174uscnasn05', 'swoole_session_name':'OX4PrTzt5s0EeGK7xFfO2tQDey'}
data1={'openid':'oKvvajr2WacI-GN7tGzsNjnZGpds','dev_sn':'808000223163'}
dataopen={'openid':'oKvvajr2WacI-GN7tGzsNjnZGpds','dev_sn':'808000223163','temp':'10','mode':'1','direct':'0','wind':'0','onoff':'0','key':'0'}
dataclose={'openid':'oKvvajr2WacI-GN7tGzsNjnZGpds','dev_sn':'808000223163','temp':'10','mode':'1','direct':'0','wind':'0','onoff':'1','key':'0'}




u='http://wechat.ifanscloud.com'

url ='/wxpub/wukong/air_condition/query_run_status'
#r=requests.post(u+url,headers=header,params=pa,data=data1,cookies=C)
#print(r.text)
#print(r.request)
pac={'action':'put','v':'1500288518955'}
urlswtich='/wxpub/wukong/air_condition/air_ctrl'
pao={'action':'put','v':'1500288514773'}
#r=requests.post(u+url,headers=header,params=pac,data=dataclose,cookies=C)
urlpower='/wxpub/wukong/stat/ele_info'
papower ={'action':'get','v':'1500288534578'}
datapower = {'dev_sn':'808000223163'}
pao={'action':'put','v':'1500288514773'}
#r=requests.post(u+url,headers=header,params=pao,data=dataopen,cookies=C)
#print(r.text)
# print(r.text)
# print(r.request.headers)
# print(r.request.data)
def open():
    try:
        r=requests.post(u+urlswtich,headers=header,params=pao,data=dataopen,cookies=C)
        log(0,'debug',r.text)
        b=-3
    
        if r.status_code != 200: 
            b= -2
        else:
            rj= json.loads(r.text)
            if (rj.get('result')=='success'):
                b=rj.get('data').get('onoff')
                t=rj.get('data').get('temperature')
                if b is None:
                    b= -1
        log(1,'open',str(b)+','+str(t))
    except Exception as e:
        log(2,"except",str(e))
        return -3            
    return  b

def close():
    try:
        r=requests.post(u+urlswtich,headers=header,params=pac,data=dataclose,cookies=C)
        log(0,'debug',r.text)
        b=-3
        t= -3
        if r.status_code != 200: 
            b= -2
        else:
            rj= json.loads(r.text)
            if (rj.get('result')=='success'):
                b=rj.get('data').get('onoff')
                t=rj.get('data').get('temperature')
                if b is None:
                    b= -1
        log(1,'close',str(b)+','+str(t)) 
    except Exception as e:
        log(2,"except",str(e))
        return -3                
    return  b

def power():
    try:
        p=-2
        r=requests.post(u+urlpower,headers=header,params=papower,data=datapower,cookies=C)
        log(0,'debug',r.text)
    #    print(r.text)
    #    log(2,'status',r.text)
        rj=json.loads(r.text)
        if rj.get('result') =='success':
            p=rj.get('data').get('curr_power')
            p = p/1000
            if p is None:
                p=-1
    except Exception as e:
        log(2,"except",str(e))
        return -3        
    return p   


online = -2 
onoff  =-2 
temp   =-2 
openstatus = 'NULL'

def status():
    global online
    global onoff    
    global temp 
    try:
        r=requests.post(u+url,headers=header,params=pa,data=data1,cookies=C)
    #     print(r.text)
        rj=json.loads(r.text)
        if rj.get('result') =='success':
            onoff=rj.get('data').get('onoff')
            online = rj.get('data').get('online')
            temp = rj.get('data').get('temperature')
            if onoff is None:
                onoff = -1
            if online is None:
                online =-1
            if temp is None:
                temp = -1
    except Exception as e:
        log(2,"except",str(e))
        return -3        

def powerm(seconds):
    while True:
        log(1,'power',str(power()))
        time.sleep(seconds)

def autoswtich(seconds,t):
    global online
    global onoff    
    global temp 
    while True:
        if (datetime.now().hour>17) or (datetime.now().hour < 10):
            status()
            log(1,'status',str(online)+','+str(onoff)+','+str(temp))
            if temp >0:
                if temp <= t:
                    if onoff != 5:
                        for i in range(1,5):
                            if onoff == 1:
                                if power()>15:
                                    open()
                                    status()
                            
                            if onoff == 0:
                                if close()==1:
                                    break
                            time.sleep(2)                
                if temp >= t+1:
                    if onoff != 5:
                        for i in range(1,5):
                            if onoff == 0:
                                if power()<=15:
                                    close()
                                    status()
                            
                            if onoff == 1:
                                if open()==0:
                                    break
                            time.sleep(2)
            time.sleep(seconds)    
            
    
    

if __name__ == '__main__':
    config_info = {
            'monitor':5,
            'powerstatistics':1
    }

#     threading.Thread(target=timer, args=(close, config_info['monitor'])).start()
    tarray=[]
    t1=threading.Thread(target=powerm, args=(120,))
    tarray.append(t1)
    t2=threading.Thread(target=autoswtich, args=(60,27))
    tarray.append(t2)
    for t in tarray:
        t.start()
    for t in tarray:
        t.join()
#     while True:
#         time.sleep(1)

        
    
