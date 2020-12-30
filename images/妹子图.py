import requests
import parsel


# 处理相册url
def get_url():
    # 数据转换+url请求
    reg = parsel.Selector(requests.get(url=url, headers=headers).text)
    # 提取每个相册的url
    href = reg.xpath('//ul[@id="pins"]/li/a/@href').getall()
    # 将提取的相册url返回出去
    return href


# 处理第二层的内容
def pins(href):
    abc = 0
    # 遍历数组中的url
    for i in href:
        # 请求第二层的url
        html_data = parsel.Selector(requests.get(url=i, headers=headers).text)
        # 提取第二层的页码
        mun = html_data.xpath('//div[@class="pagenavi"]/a[5]/span/text()').getall()[0]
        # 生成每个图片的详情url
        for _base_url in range(1, int(mun) + 1):
            x = parsel.Selector(requests.get(url=i + '/{}'.format(_base_url), headers=headers).text)
            images = x.xpath('//div[@class="main-image"]/p/a/img/@src').getall()[0]
            abc = abc + 1
            # with open(r'./IMG/' + '%s' % abc + '.' + images.split('.')[-1], mode='wb')as f:
            #     f.write(requests.get(url=images, headers=headers).content)
            #     print(abc)
            print(images)


if __name__ == '__main__':
    url = 'https://www.mzitu.com/xinggan/'
    headers = {
        'referer': 'https://www.mzitu.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 '
                      'Safari/537.36 '
    }
    # 调用函数
    pins(get_url())
