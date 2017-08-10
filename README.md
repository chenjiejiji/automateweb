## 功能
利用python+unittest编写自动化测试case脚本，先封装了webdriver的中定位方式 浏览器启动方式 自动化测试case都调用封装好的架构中webdriverAPI类，这样做的好处如果webdriver官方有修改 废弃一些接口的时候只需要修改少量的代码就可以使脚本正常运行。
在编写每一个testcase过程中一定记住低耦合，这样在后期维护的时候维护成本可以达到最小。testcase的测试数据做成数据驱动，方便production environment和Testing environment自由切换。
Jinja2生产本次测试报告并上传远程测试服务器。

## 依赖

 Jinja2
 paramiko

windows下
直接运行 install.bat 安装依赖

##有问题反馈
在使用中有任何问题，欢迎反馈给我，可以用以下联系方式跟我交流

* 邮件(chenjiejiji#gmail.com, 把#换成@)
* QQ: 539901741
* 作者:bob_jie

##结构
```javascript
	-selenium
	--config 		---__init__.py
	--testcode 		---__init__.py
					--- testinit.py(测试用运行脚本)
	--testreport	---__init__.py
					---info 			----AutoMade.txt（测试报告信息）
					---report 			----201705230926.html（生产的测试报告）
										----HTML.html（测试报告的模板）
					---SHHHtmlAPI.py(测试报告上传远程服务器)
					---WriteHtmlApi.py（生产测试报告）
					---WriteTxtApi.py （生产测试报告的信息）
	--webdriverlibs 
					---__init__.py
					---WebdriverApi.pyi（二次封装的webdriver的类）
	--123.bat
```

##启动
123.bat
  