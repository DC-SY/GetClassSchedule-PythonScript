from lxml import etree


def parse_table(path: str) -> list:
    with open(path, 'r', encoding='utf-8') as file:
        html = file.read()
    html_tree = etree.HTML(html)
    # 设置数据列表
    # 课程列表，如果没有课程就填入空字符串
    course: list = []
    # 上课时间
    period: list = []
    # 上课地点
    place: list = []
    # 任课教师
    teacher: list = []
    semester = html_tree.xpath('//h6/text()')[0]
    # 星期
    week = []
    print(f"\t->第一遍数据清洗")
    for td in html_tree.xpath('//td[@class="td_wrap"]/div[@class="timetable_con text-left"]'):
        data = td.xpath('.//text()')
        data1 = td.xpath('../@id')
        if len(data) <= 0:
            return []
        course.append(data[0].replace('\n', '').strip().replace('▲', '').replace('【调】', ''))
        period.append(data[1][7:].replace('\n', '').strip().replace('周', ''))
        place.append(data[2].replace('\n', '').strip().replace('无锡校区  ', ''))
        teacher.append(data[3].replace('\n', '').strip())
        week.append(data1[0].replace('\n', '').strip())
    """
    对数据进行完整性检查
    pass
    """
    if len(course) == len(period) == len(place) == len(teacher) == len(week) and len(course) <= 35:
        # print("课程列表:", len(course), course)
        # print("上课周数:", len(period), period)
        # print("上课地点:", len(place), place)
        # print("任课教师:", len(teacher), teacher)
        # print("课程时段:", len(week), week)
        """
        对周数进行处理：
        1. 1-16
        2. 2-16(双)
        3. 1-15(单)
        4. 1-3(单),4-16
        5. 4
        """
        print(f"\t->第二遍数据清洗")
        for i in range(len(period)):
            # 按照逗号进行分类处理
            if ',' not in period[i]:
                if '单' in period[i]:
                    a, b = str(period[i]).replace('(单)', '').split('-')
                    period[i] = list(range(int(a), int(b) + 1, 2))
                elif '双' in period[i]:
                    a, b = str(period[i]).replace('(双)', '').split('-')
                    period[i] = list(range(int(a), int(b) + 1, 2))
                elif '-' not in period[i]:
                    period[i] = int(period[i])
                else:
                    a, b = period[i].split('-')
                    period[i] = list(range(int(a), int(b) + 1))
            else:
                new_period = period[i].split(',')
                list_: list = []
                for j in range(len(new_period)):
                    if '单' in new_period[j]:
                        a, b = str(new_period[j]).replace('(单)', '').split('-')
                        new_period[j] = list(range(int(a), int(b) + 1, 2))
                    elif '双' in new_period[j]:
                        a, b = str(new_period[j]).replace('(双)', '').split('-')
                        new_period[j] = list(range(int(a), int(b) + 1, 2))
                    elif '-' not in new_period[j]:
                        pass
                    else:
                        a, b = new_period[j].split('-')
                        new_period[j] = list(range(int(a), int(b) + 1))
                    for k in new_period[j]:
                        list_.append(int(k))
                period[i] = list_
        for i in range(len(period)):
            if not isinstance(period[i], list):
                period[i] = [period[i]]
    else:
        return []
    new_data = []
    for i in range(len(course)):
        # [课程名称，哪几周，课程地点，任课教师，学期]
        new_data.append([course[i], period[i], place[i], teacher[i], semester, week[i]])
    print(f"\t->获取到课程表内容")
    return new_data
