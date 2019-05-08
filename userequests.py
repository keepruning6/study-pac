import requests




URL= 'http://www.baidu.com'
def use_simple_requests():
	response= requests.get(URL)
	print '>>>response Headers:'
	print response.headers
	print '>>>response body'
	print response.text
	print '>>>code'
	print response.status_code
	print response.reason

if __name__=='__main__':
	print '>>>>use simple requests:'
	use_simple_requests()
