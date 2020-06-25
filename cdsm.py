import socket
import threading
import requests
import re

list_ip = []
def getIP(domain):
	myaddr = socket.getaddrinfo(domain, 'http')
	return(myaddr[0][4][0])

def xxx(host):
	url = "http://"+host
	try:
		qingqiu = requests.get(url,timeout=2)
	except:
		print(host+"连接错误")
	try:
		qingqiu.encoding = qingqiu.apparent_encoding
		wangye = qingqiu.text
		title = re.findall("<title>.*?</title>",wangye)
	except:
		pass
	try:
		w = qingqiu.headers
	except:
		pass
	xinxi = ""
	try:
		if w['server']:
			xinxi += "服务器："+w['server']
	except:
		pass
	try:
		if w['X-Powered-By']:
			xinxi += "\n信息："+w['X-Powered-By']
	except:
		pass
	try:
		if title:
			biaoti = title[0]
			biaotis = biaoti.replace("<title>","") 
			biaotiss = biaotis.replace("</title>","")
			xinxi += "\n标题:"+biaotiss
	except:
		pass
	xinxi += "\n==========================================="
	print("[+]"+"http://"+host+"\t+开启+"+"\n"+xinxi)


def ipy(host):
	q = host.split(".")
	liebiao = []
	for i in range(0,255):
		f = q[0]+"."+q[1]+"."+q[2]+"."+str(i)
		liebiao.append(f)
		
	return liebiao
	
def saomiao(host,port):
	global list_ip
	try:
		socket.setdefaulttimeout(1)
		lianjie = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		lianjie.connect((host,port))
		host_port=host+":"+str(port)
		list_ip.append(host_port)
		lianjie.close()		
	except:
		return

def cdsm_main(yuming):
	print("==进入c段扫描项==\n")
	threads = []
	ip = getIP(yuming)
	ips = ipy(ip)
	for host in ips:
		t = threading.Thread(target=main_a,args=(host,))
		threads.append(t)
		t.start()
	for i in list_ip:
		xxx(i)
	for t in threads:
		t.join()
	print("==扫描完成==\n")

def main_a(host):
	dk=80
	saomiao(host,dk)

if __name__ == '__main__':
	main()
