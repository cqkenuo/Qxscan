import requests
import re

def zymcx(host):
	header = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'
		}
	url = "https://chaziyu.com/"+host+"/"
	x = requests.get(url,headers=header)
	
	txt = x.text
	
	liebiao = re.findall("target=\"_blank\">.+?</a></td>",txt)
	print("子域名： ")
	for i in liebiao:
		i = i.replace("target=\"_blank\">","")
		i = i.replace("</a></td>","")
		i = i.strip()
		print("\t"+i)
	



def zymcx_main(host):
	print("==进入子域名查询项==\n")
	yuming = input("==>请输入域名(若当前域名直接输入[y]): ")
	
	if yuming == "y":
		zymcx(host)
	else:
		zymcx(yuming)
	print("=======查询结束=======\n")
	
