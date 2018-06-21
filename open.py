import requests

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
'Accept-Language': 'zh-CN,en-US;q=0.8'}
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
url='/wxpub/wukong/air_condition/air_ctrl'
pao={'action':'put','v':'1500288514773'}
#r=requests.post(u+url,headers=header,params=pac,data=dataclose,cookies=C)

pao={'action':'put','v':'1500288514773'}
r=requests.post(u+url,headers=header,params=pao,data=dataopen,cookies=C)
#print(r.text)
print(r.text)
print(r.request.headers)