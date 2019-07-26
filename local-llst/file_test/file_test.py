# -*- coding: utf-8 -*-
import os
import log_test.logUtils, re, json

log = log_test.logUtils.Logger(file_name='info.log', level='debug').log


def one_to_two(file_name, flag):
    log.info(os.getcwd())
    # log.debug(os.access(path=file_name, mode=os.F_OK))
    file = open(file=file_name, mode='r', encoding='utf8')
    log.info(file)
    log.info('*' * 100)
    result = file.read()
    log.info(type(result))
    log.info(result)
    file.close()
    log.info(result)
    if flag == 'zuh':
        name = 'C:\\Users\\lisongtao\\PycharmProjects\\local-llst\\file_test\\zuh.log'
        pattern = re.compile(r'data:ZxUserHistory (.*?),error:')
    else:
        name = 'C:\\Users\\lisongtao\\PycharmProjects\\local-llst\\file_test\\zdh.log'
        pattern = re.compile(r'data:ZxDsHistory (.*?),error:')
    rs = pattern.findall(result)
    print(rs)
    print(type(rs))

    try:
        with open(name, mode='a', encoding='utf8') as file:
            for i in range(len(rs)):
                # if i % 2 == 0:
                print(rs[i])
                rs[i].encode()
                file.write(rs[i])
                file.write('\n')
                print('-' * 100)
    except Exception as e:
        print(e)
    finally:
        file.close()
    log.info("done")
    pass


def read_file_to_json(file_name):
    with open(file_name, mode='r', encoding='utf8') as file:
        content = file.readlines()
        for i in range(len(content)):
            print(content[i])
            parse_str_to_json(content[i])
    pass


regex_account = 'account=(.*?),'
regex_date = 'date=(.*?),'
regex_ds_name = 'dsName=(.*?),'
regex_type = 'type=(.*?),'
regex_cid = 'type=(.*?),'
regex_card = 'type=(.*?),'
regex_name = 'name=(.*?),'
regex_mobile = 'mobile=(.*?),'
regex_email = 'email=(.*?),'
regex_charge = 'charge=(.*?),'
regex_expense = 'expense=(.*?),'
regex_result = 'result=(.*?),'
regex_tid = 'tid=(.*?),'
regex_reqTid = 'reqTid=(.*?), category'
regex_category = 'category=(.*?),'
regex_mname = 'mname=(.*?),'
regex_mid = 'mid=(.*?),'
regex_businessCode = 'businessCode=(.*?),'
regex_mType = 'mType=(.*?),'
regex_spent = 'spent=(.*?)\]'
regex_history_data = 'historyData=(.*?), result='

pattern_account = re.compile(regex_account)
pattern_date = re.compile(regex_date)
pattern_history_data = re.compile(regex_history_data)
pattern_ds_name = re.compile(regex_ds_name)
pattern_type = re.compile(regex_type)
pattern_cid = re.compile(regex_cid)
pattern_card = re.compile(regex_card)
pattern_name = re.compile(regex_name)
pattern_mobile = re.compile(regex_mobile)
pattern_email = re.compile(regex_email)
pattern_charge = re.compile(regex_charge)
pattern_result = re.compile(regex_result)
pattern_tid = re.compile(regex_tid)
pattern_reqTid = re.compile(regex_reqTid)
pattern_mname = re.compile(regex_mname)
pattern_mid = re.compile(regex_mid)
pattern_spent = re.compile(regex_spent)
pattern_mType = re.compile(regex_mType)
pattern_category = re.compile(regex_category)
pattern_businessCode = re.compile(regex_businessCode)
pattern_expense = re.compile(regex_expense)


def parse_str_to_json(text):
    data = {}
    data["account"] = pattern_account.findall(text)[0]
    data["date"] = pattern_date.findall(text)[0]
    data["historyData"] = pattern_history_data.findall(text)[0]
    data["name"] = pattern_name.findall(text)[0]
    data["cid"] = pattern_cid.findall(text)[0]
    data["tid"] = pattern_tid.findall(text)[0]
    data["dsName"] = pattern_ds_name.findall(text)[0]
    data["email"] = pattern_email.findall(text)[0]
    data["expense"] = pattern_expense.findall(text)[0]
    data["result"] = pattern_result.findall(text)[0]
    data["reqTid"] = pattern_reqTid.findall(text)[0]
    data["category"] = pattern_category.findall(text)[0]
    data["mType"] = pattern_mType.findall(text)[0]
    data["spent"] = pattern_spent.findall(text)[0]
    data["businessCode"] = pattern_businessCode.findall(text)[0]
    data["mname"] = pattern_mname.findall(text)[0]
    data["mid"] = pattern_mid.findall(text)[0]
    data["card"] = pattern_card.findall(text)[0]
    data["mobile"] = pattern_mobile.findall(text)[0]
    print(data)
    json_str = json.dumps(data, ensure_ascii=False)
    print(json_str)


if __name__ == '__main__':
    # one_to_two('C:\\Users\\lisongtao\\Desktop\\data\\0618zdh.txt', 'zdh')
    # one_to_two('C:\\Users\\lisongtao\\Desktop\\data\\0618zuh.txt', 'zuh')
    # one_to_two('C:\\Users\\lisongtao\\Desktop\\data\\0619zdh.txt', 'zdh')
    # one_to_two('C:\\Users\\lisongtao\\Desktop\\data\\0619zuh.txt', 'zuh')
    # one_to_two('C:\\Users\\lisongtao\\Desktop\\data\\0620zdh.txt', 'zdh')
    # one_to_two('C:\\Users\\lisongtao\\Desktop\\data\\0620zuh.txt', 'zuh')
    read_file_to_json('C:\\Users\\lisongtao\\PycharmProjects\\local-llst\\file_test\\zdh.log')
