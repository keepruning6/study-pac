import urllib
import urllib2




URL= 'http://www.baidu.com'
def use_simple_urllib():
	response= urllib2.urlopen(URL)
	print '>>>response Headers:'
	print response.info()
	print ''.join([line for line in response.readlines()])
	print response.getcode()

"""
def use_params_urllib2():
	params=urllib.urlencoode({'param1':'hello','param2':'world'})
    #print 'response params:'
    print params
    response=urllib2.urlopen('?'.join([URL,'%s'])%params)
    print response.info()
    print ''.join([line for line in response.readlines()])

 """
if __name__=='__main__':
	print '>>>>use simple urllib2:'
	use_simple_urllib()
