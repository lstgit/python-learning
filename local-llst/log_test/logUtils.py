import logging
from logging import handlers


class Logger(object):
    # log日志级别映射
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'error': logging.ERROR,
        'warning': logging.WARN,
        'crit': logging.CRITICAL
    }

    def __init__(self, file_name, level='info', when='D', backCount=3,
                 fmt='%(asctime)s - [%(thread)d] - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.log = logging.getLogger(file_name)
        format_str = logging.Formatter(fmt)
        self.log.setLevel(self.level_relations.get(level))
        sh = logging.StreamHandler()
        sh.setFormatter(format_str)
        # 使用处理器 把日志写入文件
        th = handlers.TimedRotatingFileHandler(filename=file_name, when=when, backupCount=backCount, encoding='utf-8')
        #  实例化TimedRotatingFileHandler
        #  interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(fmt=format_str)
        self.log.addHandler(sh)
        self.log.addHandler(th)


if __name__ == '__main__':
    log = Logger(file_name='info.log', level='debug')
    log.log.debug('dadad')
    log.log.info('adasd')
    # print('adasd')
    try:
        i = 10 / 0
    except Exception as e:
        log.log.error("error:%s" % e)
