import re
import requests
import parsel

def get_id():
    reg = requests.get(url,headers=headers).text
    reg = parsel.Selector(reg)
    video_id = reg.xpath('//*[@id="categoryList"]/li/div/a/@href').getall()
    kw = []
    for i in video_id:
        i = i.split('video_')[-1]
        kw.append(i)
    return kw


def magic(video_id):
    for i in video_id:
        base_url = 'https://www.pearvideo.com/videoStatus.jsp?contId={}&mrd=0.6050582994783404'.format(i)
        head = {
            'Referer':'https://www.pearvideo.com/video_{}'.format(i),
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        }
        regs = requests.get(url=base_url,headers=head).json()
        base_url = regs['videoInfo']['videos']['srcUrl']
        print(re.sub(r'[\d]{13}','cont-{}'.format(i),base_url))
    print('====================给爷停====================')






if __name__ == '__main__':
    print('====================给爷爬====================')
    url = 'https://www.pearvideo.com/category_8'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }
    magic(get_id())