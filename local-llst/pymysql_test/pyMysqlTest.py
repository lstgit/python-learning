import pymysql, configparser, time, json

cf = configparser.ConfigParser()
cf.read("database.ini")
li = cf.items("dbMysql")
database_info = dict(li)
print(database_info)

print(cf.options("dbMysql"))
print(cf.sections())

try:
    t1 = time.time()

    conn = pymysql.Connect(host=database_info['host'], port=int(database_info['port']),
                           user=database_info['user'], passwd=database_info['password'], db=database_info['db_name'],
                           charset='utf8')
    t2 = time.time()
    print('create conn spent %f' % (t2 - t1))
    sql = 'select * from test2 where name = %s limit 10 '
    # sql = 'select id,name,age,convert(content using utf8) as content from person where name = %s'
    # sql = 'select id,name,age,convert(content using utf8) as content from person where name = %s' % ('1 xor 1=1') # sql 注入示例
    # sql2 = "insert into person(name,age,content) values('guqin','1','渔樵问答,渔舟唱晚,平沙落雁')"
    # sql3 = 'update person set age="%d" where name="%s"' % (2, 'guqin')
    cursor = conn.cursor()
    del t1, t2
    t1 = time.time()
    cursor.execute(sql, '1 xor 1=1')
    t2 = time.time()
    print("exec spent %f" % (t2 - t1))
    # cursor.execute(sql)
    # conn.commit()
    data = cursor.fetchall()
    dic = {'result': data}
    print(json.dumps(dic))
except Exception as e:
    print(e)
finally:
    print(conn, cursor)  # conn 和 cursor 是全局变量
    if conn is not None and cursor is not None:
        print(123)
        cursor.close()
        conn.close()
