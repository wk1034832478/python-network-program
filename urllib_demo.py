from urllib.request import urlopen

webpage = urlopen( 'http://www.baidu.com' )

print('说明：', webpage.__doc__ )

text = webpage.read()
print( text )

