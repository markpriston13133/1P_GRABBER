from config import config
C=config()

from parse_rest.connection import register
register(C['APPLICATION_ID'], C['REST_API_KEY'], master_key=C['MASTER_KEY'])

from parse_rest.datatypes import Object
class ip(Object):
        pass



import urllib2



def getIP():
    try:
        response = urllib2.urlopen('http://dynupdate.no-ip.com/ip.php')
        return response.read()
    except:
        return false



actual_ip = getIP()
#actual_ip = "111.111.111.120"
thisIP = ip()
print actual_ip

if actual_ip:
    thisIP.ip = actual_ip
else:
    thisIP.ip = 'not valid'
thisIP.save()

