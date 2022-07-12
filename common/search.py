
import time
def open_url(url,driver):      #打开网址，窗口最大化
    driver.get(url)
    driver.maximize_window()

def login_page(username,password,verification_vode,driver):     #用户名，密码，验证码，登录
    driver.find_element_by_xpath('//*[@id="theForm"]/div/div[1]/div[2]/div[1]/input').send_keys(username)               #定位用户名输入
    driver.find_element_by_xpath('//*[@id="theForm"]/div/div[1]/div[2]/div[2]/input').send_keys(password)               #定位密码输入
    driver.find_element_by_xpath('//*[@id="theForm"]/div/div[1]/div[2]/div[3]/input').send_keys(verification_vode)      #定位验证码输入
    driver.find_element_by_xpath('//*[@id="theForm"]/div/div[1]/div[2]/div[5]/span/input').click()                      #定位点击登录


def search_key(url,driver,username,password,verification_vode,number):
    open_url(url,driver)
    login_page(username,password,verification_vode,driver)
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/ul/li[1]/a').click()                                         #定位点击系统
    driver.find_element_by_xpath('//div[@id="admincpNavTabs_system"]//h3[text()="会员"]').click()                        #定位点击会员
    driver.switch_to.frame(0)                                                                                           #切换子页面
    driver.find_element_by_id("search_key").send_keys(number)                                                           #定位搜索框输入手机号
    driver.find_element_by_xpath('//*[@id="search-form2"]/div/div/input[2]').click()                                    #定位点击搜索
    time.sleep(10)                                                                                                      #延时
    nume=driver.find_element_by_xpath('//div[@id="ajax_return"]//div[@style="text-align: center; width: 80px;"]').text  #取出搜索结果赋值给nume
    return nume
