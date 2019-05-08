# -*- coding:utf-8 -*- 

import requests
import json


URL='https://api.github.com'


def build_uri(endpoint):
	return '/'.join([URL,endpoint])

# 使用json让显示更加好看
def better_print(json_str):
	return json.dumps(json.loads(json_str),indent=4)


def requests_method():
	response=requests.get(URL,build_uri('user/imoocdemo'))
	print better_print(response.text)

if __name__=='__main__':
	requests_method()