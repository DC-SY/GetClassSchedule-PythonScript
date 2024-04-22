import pymysql
from openpyxl import load_workbook
from datetime import time


def save_to_excel(path: str, data: list) -> None:
    workbook = load_workbook(filename=path)
    worksheet = workbook.active
    for row in data:
        worksheet.append(str(row))
    workbook.save(path)


def save_to_database(host: str, user: str, password: str, database: str, port: str, data: list) -> bool:
    conn = pymysql.connect(
        host=host,  # 数据库主机地址
        port=int(port),  # 数据库端口号
        user=user,  # 数据库用户名
        password=password,  # 数据库密码
        db=database  # 要连接的数据库名
    )
    if not conn:
        return False
    list_1 = [
        # ["课程时段，上课时间，下课时间，周几]
        ["1-1", time(8, 0), time(9, 40), "星期一"], ["1-3", time(10, 10), time(11, 35), "星期一"], ["1-5", time(14, 0), time(15, 35), "星期一"], ["1-7", time(15, 55), time(17, 35), "星期一"], ["1-9", time(18, 45), time(20, 25), "星期一"],
        ["2-1", time(8, 0), time(9, 40), "星期二"], ["2-3", time(10, 10), time(11, 35), "星期二"], ["2-5", time(14, 0), time(15, 35), "星期二"], ["2-7", time(15, 55), time(17, 35), "星期二"], ["2-9", time(18, 45), time(20, 25), "星期二"],
        ["3-1", time(8, 0), time(9, 40), "星期三"], ["3-3", time(10, 10), time(11, 35), "星期三"], ["3-5", time(14, 0), time(15, 35), "星期三"], ["3-7", time(15, 55), time(17, 35), "星期三"], ["3-9", time(18, 45), time(20, 25), "星期三"],
        ["4-1", time(8, 0), time(9, 40), "星期四"], ["4-3", time(10, 10), time(11, 35), "星期四"], ["4-5", time(14, 0), time(15, 35), "星期四"], ["4-7", time(15, 55), time(17, 35), "星期四"], ["4-9", time(18, 45), time(20, 25), "星期四"],
        ["5-1", time(8, 0), time(9, 40), "星期五"], ["5-3", time(10, 10), time(11, 35), "星期五"], ["5-5", time(14, 0), time(15, 35), "星期五"], ["5-7", time(15, 55), time(17, 35), "星期五"], ["5-9", time(18, 45), time(20, 25), "星期五"],
        ["6-1", time(8, 0), time(9, 40), "星期六"], ["6-3", time(10, 10), time(11, 35), "星期六"], ["6-5", time(14, 0), time(15, 35), "星期六"], ["6-7", time(15, 55), time(17, 35), "星期六"], ["6-9", time(18, 45), time(20, 25), "星期六"],
        ["7-1", time(8, 0), time(9, 40), "星期日"], ["7-3", time(10, 10), time(11, 35), "星期日"], ["7-5", time(14, 0), time(15, 35), "星期日"], ["7-7", time(15, 55), time(17, 35), "星期日"], ["7-9", time(18, 45), time(20, 25), "星期日"],
    ]
    list_2: list = []
    for i in range(len(list_1)):
        for j in range(len(data)):
            if list_1[i][0] == data[j][-1]:
                print(f"\t\t->课程：{data[j][0]}配对成功")
                list_: list = []
                for a in range(len(list_1[i])):
                    list_.append(list_1[i][a])
                for b in range(len(data[j][:-1])):
                    list_.append(data[j][b])
                list_2.append(list_)
    print("\t->第三遍数据清洗")
    for i in range(len(list_2)):
        str_ = ', '.join(map(str, list_2[i][5]))
        list_2[i][5] = str_
        list_2[i][1] = list_2[i][1].strftime('%H:%M:%S')
        list_2[i][2] = list_2[i][2].strftime('%H:%M:%S')
    for i in list_2:
        print(i)
    # 创建一个 cursor 对象使用其执行 SQL 语句
    try:
        # 创建游标对象
        with conn.cursor() as cursor:
            # 创建SQL语句
            sql = f"INSERT INTO `class_schedule` (`class_period`, `class_start_time`, `class_end_time`, `class_week`, `class_name`, `class_schedule`, `class_place`,`class_teacher`, `semester` ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            # 执行SQL语句
            cursor.executemany(sql, list_2)
            # 提交事务
            conn.commit()

    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        # 关闭连接
        conn.close()
