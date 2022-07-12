from common import search               #导入封装函数文件
from test_data import test_data         #导入测试数据文件
from selenium import webdriver          #导入webdriver
driver = webdriver.Edge()               #打开浏览器
driver.implicitly_wait(10)                                        #隐式等待
url = test_data.url["url"]                                        #url取值
username = test_data.login_data["username"]                       #用户名取值
password = test_data.login_data["password"]                       #密码取值
verification_vode = test_data.login_data["verification_vode"]     #验证码取值
number = test_data.number["number"]                               #搜索手机号取值

#调用函数和传参 结果赋值给result
result = search.search_key(url=url,driver=driver,username=username,password=password,verification_vode=verification_vode,number=number)

if number in result:
    print("通过")
else:
    print("不通过")