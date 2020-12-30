import time
import requests



def graphql(api):
    # 还原短连接
    a = requests.post(url=f'https://duanwangzhihuanyuan.51240.com/web_system/51240_com_www/system/file/duanwangzhihuanyuan/get/?ajaxtimestamp={time.time()*1000}',data={"turl":"https://v.kuaishou.com/7jK6j2"}).text
    # 链接
    a = a.split('href=\"')[-1]
    a = a.split('\"')[0]
    # 视频id
    b = a.split('photo/')[-1]
    b = b.split('?fid')[0]
    '''
    # 这还原不给力
    res = requests.head('https://v.kuaishou.com/7jK6j2')
    url = res.headers.get('location')
    '''
    # 请求头
    headers = {
        "Cookie": "didv=1607675569000;kpf=PC_WEB;kpn=KUAISHOU_VISION;clientid=3;client_key=65890b29;kuaishou.web.cp.api_st=ChZrdWFpc2hvdS53ZWIuY3AuYXBpLnN0EqABBY-tbrHfeZC0fATXg3wLsG_YudgXuTX0UAxCvmWrktOOyW02XcsYIF8IrzKhG1WKN_6pnJ5lh9lKUgWCXbffPzCaFqdvrxTUngKqn_WNGW4zY5t14fGymvZxG3L7hejXl8bwxvJBMEjs6kvQbbf-rf0tO7dLeVymgAq5GfkvUlu7eOfBcvVgZ9ZMXlAtPd2OT1B8__9VRjqF36HDIt3K6xoSNcMWiBr8XGnDyvZnjGXLjMB_IiCD-K4_TcRmJP316b-LufsI5l7vT6ulGWCjzbXQvL6cxigFMAE;kuaishou.web.cp.api_ph=d6e8493c8484f6d261c89c4d161a456fe65a;userId=307738636;did=web_b5996d55a6561a59fc3c5bb386d32932;kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABBYMcYdIQ6Mp8O7cCpl_l5-lKTyv5tlYuH9JcpiOpEvO1dm3DU2s7FTbYTtJxF11CojRksQJwnEAnmfF0y9jCVkmLcR-BwNp7Hx2hCLQo9w_SMX-TLAA9l2CJh05SIgEbULeM-hNkmQy18lSuMR5ElZKfNuuWON5b559YFxLcJ9eQVtlwyjEnlG1O1Liv4ze7FRxGfI1auA5_rsSsPMKNARoSg3ZkWJHNsQvvc8vsvUksYr6BIiBBLNqyBZFNlIQAIfPx4l2LMriju_U7sSHB6l57vXAdFigFMAE;kuaishou.server.web_ph=7335f3c9bb11cd0db4e086181b197e2c7841",
        "Referer": a,
        "User-Agent": "Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/87.0.4280.66Safari/537.36"
    }
    # json表单
    payload = {
	"operationName": "visionVideoDetail",
	"variables": {
		"photoId": b,
		"page": "selected"
	},
	"query": "query visionVideoDetail($photoId: String, $type: String, $page: String) {\n  visionVideoDetail(photoId: $photoId, type: $type, page: $page) {\n    status\n    type\n    author {\n      id\n      name\n      following\n      headerUrl\n      __typename\n    }\n    photo {\n      id\n      duration\n      caption\n      likeCount\n      realLikeCount\n      coverUrl\n      photoUrl\n      liked\n      timestamp\n      expTag\n      llsid\n      __typename\n    }\n    tags {\n      type\n      name\n      __typename\n    }\n    commentLimit {\n      canAddComment\n      __typename\n    }\n    llsid\n    __typename\n  }\n}\n"
}
    # 发送请求
    reg = requests.post(url=api,json=payload,headers=headers).json()
    print(reg['data']['visionVideoDetail']['photo']['photoUrl'])


if __name__ == '__main__':
    graphql('https://video.kuaishou.com/graphql')