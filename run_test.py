#coding=utf-8
import unittest
import time
from BeautifulReport import BeautifulReport
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os
import sys
from imp import reload
import shutil
reload(sys)
# sys.setdefaultencoding('utf8')
cur_path = os.path.dirname(os.path.realpath(__file__))


def add_case(caseName="case", rule="test*.py"):
    '''第一步：加载所有的测试用例'''
    case_path = os.path.join(cur_path, caseName)  # 用例文件夹
    # 如果不存在这个case文件夹，就自动创建一个
    if not os.path.exists(case_path):os.mkdir(case_path)
    print("test case path:%s"%case_path)
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                  top_level_dir=None)
    print(discover)
    return discover


def run_case(all_case, reportName="report"):
    report_path = os.path.join(cur_path, reportName)  # 用例文件夹
    if not os.path.exists(report_path):os.mkdir(report_path)
    # report_abspath = os.path.join(report_path,"result_wei.html")
    # print("report path:%s"%report_abspath)
    runner = BeautifulReport(all_case).report(filename='result_wei.html',description=u'用例执行情况：',log_path='report')
    return runner

def get_report_file(report_path):
    '''第三步：获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print (u'最新测试生成的报告： '+lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file

def send_mail(sender, psw, receiver, smtpserver, report_file, port):
    '''第四步：发送最新的测试报告内容'''
    with open(report_file, "rb") as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = u"自动化测试报告"
    msg["from"] = sender
    # msg["to"] = psw
    msg["to"] = ";".join(receiver)
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "report.html"'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, port)
    # 用户名密码
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('test report email has send out !')

def send_all(mail_list):
    send_name = []
    send_arr = mail_list.split(";")
    for i in range(len(send_arr)):
        send_name.append(send_arr[i])
    return send_name

if __name__ == "__main__":
    all_case = add_case()   # 1加载用例
    # 生成测试报告的路径
    run_case(all_case)        # 2执行用例
    # 获取最新的测试报告文件
    # report_path = os.path.join(cur_path, "report")  # 用例文件夹
    # report_file = get_report_file(report_path)  # 3获取最新的测试报告
    # shutil.copyfile(report_file,os.path.join(cur_path, "mobiletest/templates/result_wei.html"))
