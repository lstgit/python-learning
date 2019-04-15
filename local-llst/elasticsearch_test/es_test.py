import requests, json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Content-Type': 'application/json'}


# 简单查询
def send(method, url, data):
    if method == 'get':
        rsp = requests.get(url=url)
        return rsp
    if method == 'post':
        rsp = requests.post(url, data, headers=headers)
        return rsp


if __name__ == '__main__':
    # response = send('get', 'http://192.168.70.29:9200/*', None)
    # # print(response)
    # print(response.text)
    # print(response.content)
    data = {"analyzer": "ik_max_word", "text": "手机充值"}
    da = json.dumps(data)
    response = send('post', 'http://192.168.70.29:9200/entinfo201703_180525_2nd/_analyze', da)
    state_code = response.status_code
    if state_code == 200:
        print(response.text)
