import pymysql
import os
import configparser
from pymysql.cursors import DictCursor
from DBUtils.PooledDB import PooledDB


class Config(object):
    # 读取解析config
    def __init__(self, conf_name='database.ini'):
        file_path = os.path.join(os.path.dirname(__file__), conf_name)
        self.cf = configparser.ConfigParser()
        self.cf.read(file_path)

    def _get_content(self, section):
        result = {}
        # database_info = dict(self.cf.items(section))
        for each in self.cf.options(section):
            value = self.cf.get(section=section, option=each)
            result[each] = int(value) if value.isdigit() else value
        return result


class BasePyMysqlPool(object):
    def __init__(self, host, port, user, password, db_name):
        self.db_host = host
        self.db_port = int(port)
        self.user = user
        self.password = str(password)
        self.db = db_name
        self.conn = None
        self.cursor = None


class PyMysqlPool(BasePyMysqlPool):
    # 连接池初始化
    __pool = None

    def __init__(self, section):
        # 1.获取配置文件的连接信息
        self.conf = Config()._get_content(section=section)
        # 2.初始化连接信息
        super(PyMysqlPool, self).__init__(**self.conf)
        self._conn = self.__get_conn()
        self._cursor = self._conn.cursor()

    # 连接获取
    def __get_conn(self):
        if PyMysqlPool.__pool is None:
            __pool = PooledDB(creator=pymysql,
                              mincached=1,
                              maxcached=20,
                              host=self.db_host,
                              port=self.db_port,
                              user=self.user,
                              passwd=self.password,
                              db=self.db,
                              use_unicode=True,
                              charset="utf8",
                              cursorclass=DictCursor)
            print("---- pool init ---")
        return __pool.connection()

    # 连接关闭
    def dispose(self, isEnd=False):
        if isEnd is True:
            self.end('commit')
        else:
            self.end('rollback')
        print('dispose')

    def end(self, flag):
        if flag == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()
        self._cursor.close()
        self._conn.close()
        print('conn cursor closed')

    def exec(self, sql, param=None):
        if param is None:
            self._cursor.execute(sql)
        else:
            self._cursor.execute(sql, param)
        data = self._cursor.fetchall()
        return data


def main():
    mysql_pool = PyMysqlPool("dbMysql")

    # sql = 'select convert(HISTORY_DATA using utf8) as history_Data from zx_user_history where account="apiwangjia" limit 10'

    # sql = 'select account,date,type,cid,name,mobile,convert(history_data using utf8) as history_data,tid from zx_user_history where account ="apiwangjia" limit 10'
    sql = 'select account,date,type,cid,name,mobile,convert(history_data using utf8) as history_data,tid from zx_user_history where account =%s order by  date desc limit 10 '
    data = mysql_pool.exec(sql, 'apiwangjia')
    for each in data:
        print(each)
    mysql_pool.dispose()


if __name__ == '__main__':
    main()
