import os
from selenium import webdriver
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def insert_img(driver, filename):
    # 获取当前模块所在的路径
    func_path = os.path.dirname(__file__)
    # 获取test_case所在路径
    base_dir = os.path.dirname(func_path)
    # 将路径转换为字符串
    base_dir = str(base_dir)
    # 对路径的字符串进行替换
    base_dir = base_dir.replace("\\", "/")
    # 获取项目文件根目录的路径
    base = base_dir.split('/Website')[0]
    # 指定截图存放路径
    filepath = base + '/Website/test_report/screenshot/' + filename
    driver.get_screenshot_as_file(filepath)


'''if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
    insert_img(driver, 'baidu.png')
    driver.quit()
'''