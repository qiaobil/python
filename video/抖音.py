# 第三方请求库
import requests

def ids(url):
    # 还原短链接
    base_url = requests.head(url)
    base_url = base_url.headers.get('location')
    # 匹配视频的ID
    video_id = base_url.split('video/')[-1]
    video_id = video_id.split('/')[0]
    # 返回数据
    return video_id


def get_video(video_id, api):
    # 拼接完整url
    url = api + video_id
    # 请求头
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
    # 发送请求
    reg = requests.get(url=url, headers=headers).json()
    # 提取视频链接
    video_url = reg['item_list'][0]['video']['play_addr']['url_list'][0]
    video_url = video_url.replace('playwm', 'play')
    # 打印链接 ps：提取出来的视频链接需要还原链接
    print(video_url)


if __name__ == '__main__':
    # 调用函数 第一个是短视频链接，第二个是抖音官方解析接口
    get_video(ids('https://v.douyin.com/JgAwR34/'), 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=')
