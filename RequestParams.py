# -*- coding:utf-8 -*- 

import requests
import json


URL='https://api.github.com'


def build_uri(endpoint):
	return '/'.join([URL,endpoint])

# 使用json让显示更加好看
def better_print(json_str):
	return json.dumps(json.loads(json_str),indent=4)

#使用get传参可以直接后面接上params接上一个字典
def requests_params():
	response=requests.get(build_uri('users'),params={'since':11})
	print better_print(response.text)
	print response.headers
	print response.status_code
	print response.url 

#使用patch上传参数修改内容可以使用json格式上传，其中auth表示认证的内容
def request_json():
	response=requests.patch(build_uri('user'),auth=
		('imoocdemo','imoocdemo123'),json={'name':'babymoooc3'})
	print better_print(response.text)
	print response.headers
	print response.status_code


#使用post传参数可以可以使用data格式上传
def request_post():
	response=requests.post(build_uri('user/emails'),auth=
		('imoocdemo','imoocdemo123'),json=['helloworld@github.com'])
	#在上述url中可以看到这里需要给post参数一个json格式来增加一条邮件记录
	print better_print(response.text)
	print response.headers
	print response.status_code




if __name__=='__main__':
	requests_params()
	request_json()
	request_post()