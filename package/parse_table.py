from lxml import etree


def parse_table(path: str) -> list:
    with open(path, 'r', encoding='utf-8') as file:
        html = file.read()
    html_tree = etree.HTML(html)
    # 设置数据列表
    # 课程列表，如果没有课程就填入空字符串
    course = []
    # 上课时间
    period = []
    # 上课地点
    place = []
    # 任课教师
    teacher = []
    # 单双周
    frequency = []
    # 星期
    week = []
    for td in html_tree.xpath('//td[@class="td_wrap"]/div[@class="timetable_con text-left"]'):
        data = td.xpath('.//text()')
        data1 = td.xpath('../@id')
        # print(data)
        # print(len(data))
        if len(data) > 0:
            # print(data)
            course.append(data[0].replace('\n', '').strip())
            period.append(data[1].replace('\n', '').strip())
            place.append(data[2].replace('\n', '').strip())
            teacher.append(data[3].replace('\n', '').strip())
            week.append(str(data1).replace('\n', '').strip())
    """
    对数据进行完整性检查
    pass
    """
    # print("课程列表:", len(course), course)
    # print("上课时间:", len(period), period)
    # print("上课地点:", len(place), place)
    # print("任课教师:", len(teacher), teacher)
    new_data = []
    for i in range(len(course)):
        new_data.append([course[i], period[i], place[i], teacher[i], week[i]])
    print(f"\t获取到课程表内容")
    return new_data


# parse_table("../../data/data.html")
