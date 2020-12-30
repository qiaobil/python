import requests


def main():
    reg = requests.get(url,params=string,headers=head).json()
    items = reg['data']['items']
    for i in items:
        print(i['picUrl'])


if __name__ == '__main__':
    for mun in range(0,336,48):
        url = 'https://pic.sogou.com/napi/pc/searchList?'
        string = {
            "mode": "1",
            "start": "{}".format(mun),
            "xml_len": "48",
            "query": "蕾姆"
        }
        head = {
            "Referer": "https://pic.sogou.com/pics?query=%E5%8F%AF%E7%88%B1%E7%9A%84%E7%8C%AB",
            "User-Agent": "Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/87.0.4280.66Safari/537.36",

        }
        main()
