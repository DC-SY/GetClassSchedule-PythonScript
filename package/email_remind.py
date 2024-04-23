import smtplib
from datetime import datetime, timedelta, time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(data: list, sender_mail: str, sender_pass: str, receiver_mails: list, html: str) -> None:
    """
    发送邮件函数
    :param data: 发送的数据列表
    :param sender_mail: 发送邮件的邮箱
    :param sender_pass: 发送邮件的邮箱密码
    :param receiver_mails: list[str]: 接收邮件的邮箱列表
    :param html: 邮件模板
    :return: None
    """
    # 创建邮件对象和设置邮件头部信息
    for receiver_mail in receiver_mails:
        message = MIMEMultipart()
        message['From'] = sender_mail
        message['To'] = receiver_mail
        message['Subject'] = "课程通知"
        body = MIMEText(html, 'html')
        message.attach(body)

        try:
            # 使用SMTP_SSL连接服务器
            with smtplib.SMTP_SSL('smtp.feishu.cn', 465) as server:
                server.login(sender_mail, sender_pass)
                server.sendmail(sender_mail, receiver_mail, message.as_string())
                print(f"{receiver_mail}邮件发送成功")
        except Exception as e:
            print(f"{receiver_mail}邮件发送失败，错误信息：{e}")


def send_regularly():
    # dict_date = {
    #     "第一周": datetime(2024, 2, 26, 0, 0),
    #     "第二周": datetime(2024, 3, 4, 0, 0),
    #     "第三周": datetime(2024, 3, 11, 0, 0),
    #     "第四周": datetime(2024, 3, 18, 0, 0),
    #     "第五周": datetime(2024, 3, 25, 0, 0),
    #     "第六周": datetime(2024, 4, 1, 0, 0),
    #     "第七周": datetime(2024, 4, 8, 0, 0),
    #     "第八周": datetime(2024, 4, 15, 0, 0),
    #     "第九周": datetime(2024, 4, 22, 0, 0),
    #     "第十周": datetime(2024, 4, 29, 0, 0),
    #     "第十一周": datetime(2024, 5, 6, 0, 0),
    #     "第十二周": datetime(2024, 5, 13, 0, 0),
    #     "第十三周": datetime(2024, 5, 20, 0, 0),
    #     "第十四周": datetime(2024, 5, 27, 0, 0),
    #     "第十五周": datetime(2024, 6, 3, 0, 0),
    #     "第十六周": datetime(2024, 6, 10, 0, 0),
    # }
    # dict_time = {
    #     datetime
    # }
    start_date = datetime(2024, 2, 26, 0, 0)
    now_time = datetime.now()
    # 获取本周周数
    week_number = 0
    while start_date < now_time:
        start_date += timedelta(weeks=1)
        week_number += 1
    print(f"现在是第{week_number}周")
    # 获取当日周几
    day_week = now_time.weekday() + 1
    print(f"现在是周{day_week}")

    start_time = time(8, 0)
    now_hour = now_time.hour
    if 0 < (now_hour - start_time.hour) < 2:
        pass

    pass


# def email_demo(data: list, sender_mail: str, sender_pass: str, receiver_mail: list, smtp_host: str, smtp_port: str) -> None:
#     """
#     邮件提醒模块
#     :param smtp_host: 主机
#     :param smtp_port: 端口
#     :param receiver_mail: 接受者邮箱列表
#     :param sender_pass: 发送者邮箱密码
#     :param sender_mail: 发送这邮箱
#     :param data: 提醒内容列表
#     :return: None
#     """
#
#     # 创建邮件对象和设置邮件头部信息
#     message = MIMEMultipart()
#     message['From'] = sender_mail
#     message['To'] = receiver_mail
#     message['Subject'] = "课程通知"
#     body = MIMEText(str(data), 'plain')
#     message.attach(body)
#
#     try:
#         # 使用SMTP_SSL连接服务器
#         with smtplib.SMTP_SSL('smtp.feishu.cn', 465) as server:
#             server.login(sender_mail, sender_pass)
#             server.sendmail(sender_mail, receiver_mail, message.as_string())
#             print("邮件发送成功")
#     except Exception as e:
#         print(f"邮件发送失败，错误信息：{e}")


if __name__ == '__main__':
    send_regularly()
