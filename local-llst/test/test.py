# coding=utf-8

import requests
import log_test.logUtils as logger, hashlib, uuid, time, json


def post_form(url):
    data = {}
    credit = {}
    head = {}
    body = {}
    # mac 是head和body的MD5值
    head['version'] = '0100'
    head['testFlag'] = '1'
    head['activityCode'] = '1005'
    head['actionCode'] = '0'
    head['reqSys'] = 'zhongchengxin002'
    head['reqTransID'] = str(uuid.uuid1()).replace('-', '')
    head['reqDate'] = time.strftime("%Y%m%d", time.localtime(time.time()))
    head['reqDateTime'] = time.time()
    head['authorizationCode'] = ''
    body['companyName'] = ''
    body['companyTel'] = ''
    body['companyAddr'] = ''
    body['extendParam'] = ''
    mac = test()
    credit['header'] = json.dumps(head)
    credit['body'] = json.dumps(body)
    credit['mac'] = mac
    response = requests.post(url=url, data=json.dumps(credit), headers=headers, timeout=10, verify=False)
    log.info(response.status_code)
    pass


def test():
    head = {}
    body = {}
    # mac 是head和body的MD5值
    header = {}
    head['version'] = '0100'
    head['testFlag'] = '1'
    head['activityCode'] = '1005'
    head['actionCode'] = '0'
    head['reqSys'] = 'zhongchengxin002'  # 发起系统是什么?
    head['reqTransID'] = str(uuid.uuid1()).replace('-', '')
    head['reqDate'] = time.strftime("%Y%m%d", time.localtime(time.time()))
    head['reqDateTime'] = time.time()
    head['authorizationCode'] = ''  # 授权号是什么?
    body['companyName'] = ''
    body['companyTel'] = ''
    body['companyAddr'] = ''
    body['extendParam'] = ''
    mdJson = json.dumps({'header': json.dumps(head), 'body': json.dumps(body)})
    md = hashlib.md5()
    log.info(mdJson)
    md.update(mdJson.encode())
    log.info(md.hexdigest())
    return md.hexdigest()


log = logger.Logger(file_name='test.log', level='debug').log
url = 'https://apitest.tycredit.com/credit-front-http/unified/work.json'
account = 'zhongchengxin002'
home_key = '6bbc9f4ccfb617c1'
key = '6de43f218e46e28e'
test_flag = 1

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Content-Type': 'application/json'}

if __name__ == '__main__':
    post_form(url=url)
    # uid = uuid.uuid1()
    # log.info(type(uid))
    # uuid
    # str_uid = str(uid).replace('-', '')
    # log.info(str_uid)
    # local_time = time.localtime(time.time())
    # time_str = time.strftime("%Y%m%d", local_time)
    # log.info(time_str)
    # test()
