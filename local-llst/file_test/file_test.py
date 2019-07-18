import os
import log_test.logUtils, re

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


if __name__ == '__main__':
    one_to_two('C:\\Users\\lisongtao\\Desktop\\data\\0618zdh.txt', 'zdh')
    one_to_two('C:\\Users\\lisongtao\\Desktop\\data\\0618zuh.txt', 'zuh')
    one_to_two('C:\\Users\\lisongtao\\Desktop\\data\\0619zdh.txt', 'zdh')
    one_to_two('C:\\Users\\lisongtao\\Desktop\\data\\0619zuh.txt', 'zuh')
    one_to_two('C:\\Users\\lisongtao\\Desktop\\data\\0620zdh.txt', 'zdh')
    one_to_two('C:\\Users\\lisongtao\\Desktop\\data\\0620zuh.txt', 'zuh')
