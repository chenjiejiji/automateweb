#! usr/bin/python
#coding=utf-8   //这句是使用utf8编码方式方法， 可以单独加入python头使用。
# -*- coding:cp936 -*-

import os
import time
import sys 
sys.path.append('../') #解决包无法引用的问题i
from testreport import WriteTxtApi
from testreport import SHHHtmlAPI
reload(sys)
sys.setdefaultencoding( "utf-8" )
from jinja2 import Template
#jinjia2传递的参数格式 {items:[{neme:1,name:2},{neme:3,name:4}]}
#Purpose:读取信息的代码
#
#
#Author：bob jie
#2017.05.18


class WriteHtmlApi():
	def InitReadInfo(self):
		try:
			self.TestInfo = WriteTxtApi.WriteTxtApi()
			self.MoveHtml = SHHHtmlAPI.SHHHtmlApi()
			self.TestInfoes = self.TestInfo.InitReadTxt()
			self.HeadInfoes = self.TestInfo.InitReadInfo()
			FileHtml = open(os.path.abspath('..')+"/testreport/report/HTML.html","r")
			template = Template(FileHtml.read())
			data={}
			data['items']=self.TestInfoes
			# FileHtmlNEW = open(os.path.abspath('..')+"/testreport/report/HTMLnew.html","w")
			# filepath = self.InitTime()+u"/唐唐人才网"+time.strftime('%H%M%S',time.localtime())+".html"
			filename = time.strftime('%Y%m%d%H%M',time.localtime())+".html"
			filepath = self.InitTime()+'/'+filename
			FileHtmlNEW = open(filepath,"w")
			# print self.InitTime()+u"/唐唐人才网"+time.strftime('%H%M%S',time.localtime())
			FileHtmlNEW.write(template.render(autonumber=self.HeadInfoes['autonumber'],blackboxnumber=self.HeadInfoes['blackboxnumber'],successrate=self.HeadInfoes['successrate'],**data))
			#FileHtmlNEW.write(template.render(**data))
			#传递文件到服务器上
			self.MoveHtml.InitShhInfo(filepath,filename)
			self.TestInfo.InitDeleteTxt()
		except Exception,e:
			print e




	def InitTime(self):
		# a = time.localtime()
		# print time.strptime(a,'%Y%m%d')
		# print time.strftime('%Y%m%d',time.localtime())
		#判断当前路径下是否有这样的文件
		# print os.path.abspath('..')+time.strftime('%Y%m%d',time.localtime())
		# filepath=os.path.abspath('..')+'/testreport/'+time.strftime('%Y%m%d',time.localtime())
		filepath=os.path.abspath('..')+'/testreport/report'
		if os.path.exists(filepath) == False:
			os.makedirs(filepath)
		else:
			pass
		return filepath

    



if __name__ == '__main__':
	WriteHtmlApi().InitReadInfo()
	# WriteHtmlApi().InitDelete()