import re
import requests


def get_html(url):
    head = {
        "Cookie": "didv=1607675569000;clientid=3;client_key=65890b29;kpn=GAME_ZONE;kuaishou.web.cp.api_st=ChZrdWFpc2hvdS53ZWIuY3AuYXBpLnN0EqABBY-tbrHfeZC0fATXg3wLsG_YudgXuTX0UAxCvmWrktOOyW02XcsYIF8IrzKhG1WKN_6pnJ5lh9lKUgWCXbffPzCaFqdvrxTUngKqn_WNGW4zY5t14fGymvZxG3L7hejXl8bwxvJBMEjs6kvQbbf-rf0tO7dLeVymgAq5GfkvUlu7eOfBcvVgZ9ZMXlAtPd2OT1B8__9VRjqF36HDIt3K6xoSNcMWiBr8XGnDyvZnjGXLjMB_IiCD-K4_TcRmJP316b-LufsI5l7vT6ulGWCjzbXQvL6cxigFMAE;kuaishou.web.cp.api_ph=d6e8493c8484f6d261c89c4d161a456fe65a;userId=307738636;did=web_b5996d55a6561a59fc3c5bb386d32932;userId=307738636;kuaishou.live.bfb1s=477cb0011daca84b36b3a4676857e5a1;kuaishou.live.web_st=ChRrdWFpc2hvdS5saXZlLndlYi5zdBKgATSb3VkpCwlmypCEHv3fuJih1PmyE0ZSPG3_-2kekTcUeT7nM6xTe84u18DKeiH7xU-VTsJSlOdPdz_UToH6mcH2rVxvnJpy1N84EVYBCPbWSXTEyWxue5GYItTxGchr9sKwojuaH52HwuethX-feQZNcG1pmfq3hHkt7iwdcbCNsGmIivPLvWfXmESEbKXXkp0Xvne8meZas-DQf43fUeAaEurKvNghXkU0vIm_W_UXPUfuwSIggPqkduQK68CgcjIFzjF3ZcocoF9AJCfIJ-bN19ZjlhAoBTAB;kuaishou.live.web_ph=d0546aaa818c5fc27969a2284b6610dd4931;ktrace-context=1|MS42OTc4Njg0NTc2NzM4NjY5LjI3NDc4Nzg2LjE2MDg4NjU1Nzc5MTguNTcxMDg=|MS42OTc4Njg0NTc2NzM4NjY5LjM0ODU1NzM2LjE2MDg4NjU1Nzc5MTguNTcxMDk=|0|kuaishou-frontend-live|webservice|false|NA",
        "User-Agent": "Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/87.0.4280.66Safari/537.36"
    }
    reg = requests.get(url,headers=head).text
    # reg = re.findall(r'<div.class=\"long-mode\"(.*?)</div>')
    reg = re.findall(r'http://tx2\.a\.yximgs\.com/ufile/atlas/[0-9a-zA-Z]{44}_\d{1}\.webp',reg)
    mun = len(reg) - 1
    for i in reg:
        print(i)

get_html('https://live.kuaishou.com/u/Yang2010904/3x6sksgjevcfauq?did=web_e90540fa7a8c76601515b6fb13b17a2f')