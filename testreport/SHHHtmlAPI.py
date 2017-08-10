#! usr/bin/python
#coding=utf-8   //这句是使用utf8编码方式方法， 可以单独加入python头使用。
# -*- coding:cp936 -*-

from selenium import webdriver
import time
import paramiko
import datetime
import sys,os
reload(sys)
sys.setdefaultencoding( "utf-8" )
sys.path.append('../') #解决包无法引用的问题


#Purpose:上传SSH功能代码
#
#
#Author：bob jie
#2017.05.16

class SHHHtmlApi(object):
	def __init__(self):
		#服务器名称
		self.hostname='192.168.1.143'
		#用户名
		self.username='root'
		#密码
		self.password='chenjie123456'
		#端口号
		self.port=22

	def InitShhInfo(self,local_dir, remote_dir):
		try:
			t = paramiko.Transport((self.hostname,self.port))
			t.connect(username=self.username, password=self.password)
			sftp = paramiko.SFTPClient.from_transport(t)
			remotepath=remote_dir
			localpath=local_dir
			sftp.put(local_dir,"/data/UIAuto/"+remote_dir)
			t.close()
			print "**************************************"
			print "***********html  ftp  success********"
			print "**************************************"
		except Exception,e:
			print e

		#!/usr/bin/pytho



# if __name__ == '__main__':
# 	#本地上传的目录
# 	local_dir='F:/tangtangnet.com/testreport/report/201705221118.html'
# 	#远程上传的目录
# 	remote_dir='/data/UIAuto/201705221118.html'
# 	SHHHtmlAPI().InitShhInfo(local_dir,remote_dir)