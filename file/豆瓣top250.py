'''
豆瓣电影 Top 250
'''


import requests
import parsel


def N():
    a = parsel.Selector(requests.get(url=url, headers=headers).text)
    # 电影名称
    b = a.xpath('//ol[@class="grid_view"]/li/div/div/div/a/span[1]/text()').getall()
    # 电影评分
    c = a.xpath('//ol[@class="grid_view"]/li/div/div[2]/div[2]/div/span[2]/text()').getall()
    # 电影评价
    d = a.xpath('//ol[@class="grid_view"]/li/div/div[2]/div[2]/div/span[4]/text()').getall()
    # 电影个签
    e = a.xpath('//*[@class="inq"]/text()').getall()
    print(b, c, d, e)


if __name__ == '__main__':
    for i in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(i)
        headers = {
            "Referer": "https://movie.douban.com/top250?start=0",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
        }
        N()