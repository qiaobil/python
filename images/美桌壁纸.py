import requests
import parsel


def code(href):
    for demo in href:
        content = requests.get(url=demo).text
        demo = parsel.Selector(content)
        src_url = demo.xpath('//*[@id="scroll"]/li/a/@href').getall()
        for ids in src_url:
            ids = requests.get(url=ids).text
            ids = parsel.Selector(ids)
            ids = ids.xpath('//*[@class="pic-meinv"]/a/img/@src').getall()[0]
            print(ids)


def get_url():
    reg = requests.get(url).text
    html = parsel.Selector(reg)
    base_url = html.xpath('//div[@class="tab_tj"]//ul/li/a/@href').getall()
    return base_url


if __name__ == '__main__':
    for i in range(1, 6):
        url = 'http://www.win4000.com/wallpaper_0_0_0_{}.html'.format(i)
        code(get_url())
