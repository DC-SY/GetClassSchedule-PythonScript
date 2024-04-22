import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_html(username: str, password: str, path: str) -> None:
    """
    启动无头浏览器，模拟登录指定网站，并抓取页面源代码。

    参数:
    - username: 用户名，用于网站登录。
    - password: 密码，用于网站登录。
    - path: 保存抓取的页面源代码的文件路径。

    返回值:
    无
    """
    print(f"\t->启动浏览器无头模式")
    chrome_options = webdriver.ChromeOptions()
    # 设置浏览器为无头模式
    chrome_options.add_argument("--headless")
    # 禁用 GPU 加速，以提高在无头模式下的性能
    chrome_options.add_argument("--disable-gpu")
    # 降低资源使用限制，以便在资源受限的环境中运行
    chrome_options.add_argument("--disable-dev-shm-usage")
    # 设置浏览器窗口大小，以适应特定的网页布局
    chrome_options.add_argument("window-size=1920x1080")
    # 指定 Chrome 驱动的路径，并启用无头模式
    driver = webdriver.Chrome(executable_path=r'bin/chromedriver.exe', options=chrome_options)

    print(f"\t->开始向服务器发送请求")
    driver.get("https://jwgl.cwxu.edu.cn/jwglxt/xtgl/login_slogin.html")

    print(f"\t->输入用户名和密码")
    # 定位并填充用户名
    driver.find_element(By.ID, "yhm").send_keys(username)
    time.sleep(1)
    # 定位并填充密码
    driver.find_element(By.ID, "mm").send_keys(password)
    time.sleep(1)
    # 提交登录表单
    driver.find_element(By.ID, "dl").click()
    time.sleep(5)
    print(f"\t->成功登录")
    # 导航到课表查询页面
    driver.find_element(By.XPATH, "//*[contains(text(), '信息查询')]").click()
    time.sleep(1)
    print(f"\t->进入个人课表查询")

    element1 = driver.find_element(By.XPATH, "//*[contains(text(), '个人课表查询')]")
    driver.execute_script("arguments[0].click();", element1)
    print(f"\t->等待课表页面加载")
    time.sleep(10)
    # 切换到新打开的课表页面窗口
    driver.switch_to.window(driver.window_handles[1])

    print(f"\t->获取并保存课表页面源代码")
    html = driver.page_source
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    """
        这中间需要加入对数据完整行的检查，如果数据存在缺失则重新URL发起请求
        pass
    """
    driver.quit()
