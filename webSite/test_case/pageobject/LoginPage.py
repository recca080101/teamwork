from BasePage import *
from selenium.webdriver.common.by import By


# 首页登录页面
class LoginPage(Page):
    url = '/'
    # 定位器
    tet_loc = (By.ID, 'tid')
    username_loc = (By.ID, 'uid')
    password_loc = (By.ID, 'pwd')
    role_loc = (By.ID, 'urt')
    submit_loc = (By.ID, 'confirm')

    def type_tet(self, tet):
        self.find_element(*self.tet_loc).clear()
        self.find_element(*self.tet_loc).send_keys(tet)

    # 用户名输入框元素定位
    def type_username(self, username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def type_role(self, role):
        self.find_element(*self.role_loc).clear()
        self.find_element(*self.role_loc).send_keys(role)

    def type_submit(self, submit):
        self.find_element(*self.submit_loc).click()

    def login_action(self, tet, username, password, role):
        self.open()
        self.type_tet(tet)
        self.type_username(username)
        self.type_password(password)
        self.role_loc(role)
        self.type_submit()

    LoginPass_loc = (By.CLASS_NAME, 'profile-user')
    LoginFail_loc = (By.ID, 'uid')

    def type_loginPass_hit(self):
        return self.find_element(*self.LoginPass_loc).text

    def type_loginFail_hit(self):
        return self.find_element(*self.LoginFail_loc).text
