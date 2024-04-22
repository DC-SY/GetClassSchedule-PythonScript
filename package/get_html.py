import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_html(username: str, password: str, path: str) -> None:

    print(f"\t->启动浏览器无头模式")
    chrome_options = webdriver.ChromeOptions()
    # 指定无头模式
    chrome_options.add_argument("--headless")
    # 禁用 GPU 硬件加速，如果不需要绘图可以禁用
    chrome_options.add_argument("--disable-gpu")
    # 解决资源限制问题
    chrome_options.add_argument("--disable-dev-shm-usage")
    # 指定窗口大小，某些情况下有帮助
    chrome_options.add_argument("window-size=1920x1080")
    # 指定驱动程序路径，并启用无头模式
    driver = webdriver.Chrome(executable_path=r'bin/chromedriver.exe', options=chrome_options)

    print(f"\t->开始向服务器发送请求")
    driver.get("https://jwgl.cwxu.edu.cn/jwglxt/xtgl/login_slogin.html")

    print(f"\t->输入用户名和密码")
    # 定位用户名输入框,输入用户名
    driver.find_element(By.ID, "yhm").send_keys(username)
    time.sleep(1)
    # 定位到密码输入框,输入密码
    driver.find_element(By.ID, "mm").send_keys(password)
    time.sleep(1)
    # 点击登陆
    driver.find_element(By.ID, "dl").click()
    time.sleep(5)
    print(f"\t->成功登录")
    # 进入课表页面
    driver.find_element(By.XPATH, "//*[contains(text(), '信息查询')]").click()
    time.sleep(1)
    print(f"\t->进入个人课表查询")

    element1 = driver.find_element(By.XPATH, "//*[contains(text(), '个人课表查询')]")
    driver.execute_script("arguments[0].click();", element1)
    print(f"\t->课表页面加载较慢，请等待")
    time.sleep(10)
    driver.switch_to.window(driver.window_handles[1])

    print(f"\t->获取目标网页源代码")
    html = driver.page_source
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    """
        这中间需要加入对数据完整行的检查，如果数据存在缺失则重新URL发起请求
        pass
    """
    driver.quit()
