import os.path

import yaml

import package.get_html
import package.parse_table
import package.save_data
from package.email_remind import send_regularly


def main():
    with open("../config/dev.yml", 'r') as file:
        config = yaml.safe_load(file)
    os.chdir(config['root'])
    path_1 = r"data/data.html"
    print(f"1.开始解析网页源代码，保存源代码为html文件存放至{path_1}")
    package.get_html.get_html(config['website']['username'], config['website']['password'], path_1)
    print(f"2.开始解析网页源代码，保存课程表内容为list存放至列表data")
    data = package.parse_table.parse_table(path_1)
    # path_2 = r"data/data.xlsx"
    # print(f"开始解析data列表，保存课程表内容为excel存放至{path_2}")
    # package.save_data.save_to_excel(path_2, data)
    print(f"3.获取当前时间数据，发送符合日期范围的课程内容")
    send_regularly(data, config['email']['sender_mail'], config['email']['sender_pass'], config['email']['receiver_mails'])
    # package.save_data.save_to_database(config['database']['host'], config['database']['user'],
    #                                    config['database']['password'], config['database']['database'],
    #                                    config['database']['port'], data)


if __name__ == '__main__':
    main()
