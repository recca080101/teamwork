import unittest
from model import function, myunit
from pageobject.LoginPage import *
from time import sleep


class LoginTest(myunit.StartEnd):
    def test_login1_normal(self):
        print("case1 start test...")
        po = LoginPage(self.driver)
        po.login_action("zhongshan","kouqiang0002", "123qwe","降压药工厂降压药工厂-口腔科-机构管理员")
        sleep(2)
        self.assertEqual(po.type_loginPass_hit(), 'kouqiang0002')
        function.insert_img(self.driver, "case1_pass.png")
        print("case1 test end")


if __name__ == "__main__":
    unittest.main()
