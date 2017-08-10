#! usr/bin/python
#coding=utf-8   //这句是使用utf8编码方式方法， 可以单独加入python头使用。
# -*- coding:cp936 -*-


import unittest 
import sys 
sys.path.append('../') #解决包无法引用的问题
from webdriverlibs import WebdriverApi
from testreport import WriteTxtApi

#Purpose:测试封装webdriver的代码
#
#
#Author：bob jie
#2017.05.16

class mytest(unittest.TestCase): 
  ##初始化工作 
  def setUp(self): 
    #手动填写用例的中文名
    self.UseCase = u"测试测试的代码"
    #手动填写用例的自动化工程的编号
    self.AutoBoxNumber = "100001"
    #本条自动化脚本代替执行了黑盒用例的条数
    self.BlackBoxNumber = "10"

    self.Webdriver = WebdriverApi.WebdriverApi()
    self.dr = self.Webdriver.InitiaLization('Firefox')
    self.Webdriver.GetTestUrl(self.dr,'http://www.baidu.com')
    
    self.Writerinfo = WriteTxtApi.WriteTxtApi()


  #退出清理工作 
  def tearDown(self): 
    self.Webdriver.CleanBrowser(self.dr)

  #具体的测试用例，一定要以test开头 
  def testsum(self):
    if("chenjie123"=="chenjie"):
      Mode = "T"
    else:
      Mode = "F"
    print Mode
    self.assertTrue("chenjie"=="chenjie")
    self.Writerinfo.InitWriteTxt(self.UseCase,self.AutoBoxNumber,self.BlackBoxNumber,Mode)

if __name__ =='__main__': 
  unittest.main()