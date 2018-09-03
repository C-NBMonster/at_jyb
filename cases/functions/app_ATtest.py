# coding=utf-8

from selenium import webdriver
from AT_Demo.common.logger import Logger
from common.log import Log
import unittest, time,os,sys,string
from appium import webdriver

#my_logger = Logger(logger='BaiduTests').getlog()

class BaiduTests(unittest.TestCase):
    def setUp(self):
        self.log = Log("app demo test")
        self.base_url = 'http://localhost:4723/wd/hub'
        self.desired_caps = {}
        self.desired_caps['platformName']    = 'Android'
        self.desired_caps['platformVersion'] = '5.1.1'
        self.desired_caps['deviceName']  = '127.0.0.1:62025'
        #AndroidDebugBridge().call_adb('127.0.0.1:62025')  用于切换模拟器
        self.desired_caps['appPackage']  = 'com.giveu.corder'
        self.desired_caps['appActivity'] = 'com.giveu.corder.index.activity.SplashActivity'
        self.desired_caps['autoLaunch']  = 'true'
        self.desired_caps['unicodeKeyboard'] = 'true'
        self.desired_caps['resetKeyboard'] = 'true'
        #self.desired_caps['appActivity'] = 'com.giveu.corder.index.activity.WelcomeActivity'
        #.me.activity.LoginActivity}
        #print(os.path.dirname(os.getcwd()))
        self.driver = webdriver.Remote(self.base_url, self.desired_caps)
        self.driver.implicitly_wait(15)


    def test_jyb_login_demo(self):
        """即有宝登录测试用例"""
        #self.log.info("成功连接appium服务器")
        ca = self.driver.current_activity()
        print("当前activity: %s" % sys.stdout.pritn(str(ca)))
        welcome = 'com.giveu.corder.index.activity.WelcomeActivity'
        self.driver.wait_activity(welcome, 5, 1)
        self.driver.swipe(500, 500, 75, 0, 500)
        self.driver.swipe(500, 500, 75, 0, 500)


        self.driver.find_element_by_id("com.giveu.corder:id/et_account").clear()
        self.driver.find_element_by_id("com.giveu.corder:id/et_account").send_keys("865258")
        self.driver.find_element_by_id("com.giveu.corder:id/et_pwd").clear()
        self.driver.find_element_by_id("com.giveu.corder:id/et_pwd").send_keys("123456")
        self.driver.find_element_by_id("tv_login").click()
        try:
            self.driver.find_element_by_id("top_tab_center_title").is_displayed()
        except:
            self.assertEquals(1, 2, u"登录没有成功！,请查找原因")
        finally:
            tt=self.driver.find_element_by_id("top_tab_center_title").text()
            tl = tt.strip()
            self.assertEquals(tl,u"新建订单",u"jyb登录成功")
        #self.log.info("jyb登录成功")


    def tearDown(self):
        #self.log.info("关闭并退出app。")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
