#! usr/bin/python
#coding=utf-8   //这句是使用utf8编码方式方法， 可以单独加入python头使用。
# -*- coding:cp936 -*-

import os
import time
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
sys.path.append('../') #解决包无法引用的问题

#Purpose:写入txt数据的代码
#
#
#Author：bob jie
#2017.05.16


class WriteTxtApi():
	def __init__(self):
		self.Filepath = os.path.abspath('..')+"/testreport/info/AutoMade.txt"
		# self.InitDeleteTxt()

	def InitReadTxt(self):
		# FileObject = open(os.path.abspath('..')+"/testreport/info/AutoMade.txt","r")
		FileObject = open(self.Filepath,"r")
		# anter = FileObject.readline()
		# FileObject.close()
		# return anter 
		Items=[]
		for TestInfoes in  FileObject.readlines(): 
			# for In in self.TestInfoes:
			Ines = TestInfoes.split(',')
			DateDic= {
			"name":Ines[0],"nameone":Ines[1],"nametwo":Ines[2],"namethree":Ines[3]
			}
			# for In in self.TestInfoes:
			# self.Ines = In.split(',')
			# DateDic['name'] = Ines[0]
			# DateDic['nameone'] = Ines[1]
			# DateDic['nametwo'] = Ines[2]
			# DateDic['namethree'] = Ines[3]
			# print DateDic
			# print DateDic.values()
			# items.push(DateDic)
			# 直接在这里就调用生成html的代码
			Items.append(DateDic)
			# print Items
		# print Ines
		FileObject.close()
		# print Items
		return Items


	def InitWriteTxt(self,UseCase,AutoBoxNumber,BlackBoxNumber,Mode):
		#用例名称
		self.UseCase = UseCase
		#自动化用例编号
		self.AutoBoxNumber = AutoBoxNumber
		#替代执行黑盒执行的用例数
		self.BlackBoxNumber = BlackBoxNumber
		#状态
		self.Mode = Mode
		#先判断文件是否存在不存在直接创建
		# self.Filepath = os.path.abspath('..')+"/testreport/info/AutoMade.txt"
		#判断是否有这个文件
		if(os.path.exists(self.Filepath)==False):
			#用绝对地址
			# Fileobject = open(os.path.abspath('..')+"/testreport/info/AutoMade.txt","w")
			Fileobject = open(self.Filepath,"w")
			print "**************************************"
			print "***********html build success*********"
			print "**************************************"
		else:
			#用绝对地址
			# Fileobject = open(os.path.abspath('..')+"/testreport/info/AutoMade.txt","a")
			Fileobject = open(self.Filepath,"a")
		#判断是否有这个
			#windows上没有这个方法
			#os.mknod("./test.txt")
			#os.makedirs('./AutoMade.txt')
		#先判断文件是否存在不存在直接创建
		#Fileobject = open("./AutoMade.txt","w")
		#\r=windows \n=linux
		data = self.UseCase+','+self.AutoBoxNumber+','+self.BlackBoxNumber+','+self.Mode+','+'\n'
		#time.sleep(1000)
		Fileobject.write(data)
		Fileobject.close()
		print "**************************************"
		print "***********Autoinfo build success*****"
		print "**************************************"

	def InitReadInfo(self):
		itmes = self.InitReadTxt()
		HeadInfo = {}
		counts = 0
		failcounts = 0.00
		for itme in itmes:
			counts = counts + int(itme['nametwo'])
			if (itme['namethree'] == 'T'):
				failcounts =  failcounts + 1
		successper = "%.2f %%"%(failcounts/len(itmes)*100)
		
		HeadInfo['autonumber'] = len(itmes)
		HeadInfo['blackboxnumber'] = counts
		HeadInfo['successrate'] = successper
		return HeadInfo

	def InitDeleteTxt(self):
		if(os.path.exists(self.Filepath) == True):
			os.remove(self.Filepath)
			pass
		else:
			print "**************************************"
			print "**************data clear**************"
			print "**************************************"


if __name__ == '__main__':
	WriteTxtApi().InitReadInfo()
	# WriteTxtApi().InitDeleteTxt()
