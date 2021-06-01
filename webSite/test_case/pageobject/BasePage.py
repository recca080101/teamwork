from time import sleep


class Page():
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'http://10.10.2.131:8083/hiHis/index.html#'
        #self.timeout(30)

    # _open()是隐藏函数，只能在本类中使用；打开不同的子页面
    def _open(self, url):
        url_ = self.base_url + url
        print("这个页面是%s" % url_)
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        assert self.driver.current_url == url_, "不是我们要的%s" % url_

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)
