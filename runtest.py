from datetime import datetime

from selenium import webdriver
import function
import os
from HTMLTestRunner import HTMLTestRunner
import time
import unittest

from test_login import LoginTest

report_dir = "./test_report"
case_dir = "./test_case/"
case_dir1 = os.path.dirname(os.path.abspath("test_login.py"))
now = datetime.now()
case_path = os.path.join(os.path.dirname(os.path.abspath("test_login.py")))
print("start run...")
discover = unittest.defaultTestLoader.discover(case_dir1, pattern="test_login.py")
time = now.strftime("%H_%M_%S")
#date_time = now.strftime("%Y-%m-%d, %H:%M:%S")
report_name = report_dir + time + "report.html"
with open(report_name, 'wb') as f:
    runner = HTMLTestRunner(stream=f, description="localhost login", title="测试报告")
    runner.run(discover)
    f.close()
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main(verbosity=2)

    print("End run...")