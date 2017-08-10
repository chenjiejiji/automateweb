#! usr/bin/python
#coding=utf-8   //这句是使用utf8编码方式方法， 可以单独加入python头使用。
# -*- coding:cp936 -*-

from selenium import webdriver


#Purpose:封装webdriver的代码
#
#
#Author：bob jie
#2017.05.16


class WebdriverApi():
	def InitiaLization(self,browser):
		if (browser == 'Firefox'):
			self.dr = webdriver.Firefox()
			
		elif(browser == 'Chrome'):
			self.dr = webdriver.Chrome()
		elif(browser == 'IE'):
			self.dr = webdriver.Ie()
		else:
			print("参数出错")
		return self.dr

	def GetTestUrl(self,dr,URL):
		self.dr = dr
		self.URL = URL
		self.dr.get(URL)
		
	def CleanBrowser(self,dr):
		self.dr = dr
		self.dr.quit();