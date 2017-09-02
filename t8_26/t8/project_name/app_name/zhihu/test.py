# -*-coding:utf-8-*- 
from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException
# client = ZhihuClient()
# user = 'email_or_phone'
# pwd = 'password'
# try:
#     client.login('+8618375419363', 'jry123456')
#     print(u"登陆成功!")
# except NeedCaptchaException: # 处理要验证码的情况
#     # 保存验证码并提示输入，重新登录
#     with open('a.gif', 'wb') as f:
#         f.write(client.get_captcha())
#     captcha = input('please input captcha:')
#     client.login('email_or_phone', 'password', captcha)
#
# client.save_token('token.pkl') # 保存token


file=open("F:/zhihu/www.txt","w")
file.write("uef")