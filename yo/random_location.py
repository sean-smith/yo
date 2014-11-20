import urllib2
import re, json, time,hashlib, random
import MultipartPostHandler
from gevent import pool
from gevent import monkey
from urllib2 import URLError, HTTPError

monkey.patch_all()

def get_address():
    u = 100000.0
    v = 1000000.0

    longitude = int(random.gauss(116467615, u))
    latitude = int(random.gauss(39923488, u))
    print "longitude=%d,latitude=%d" % (longitude, latitude)

    url = 'http://maps.googleapis.com/maps/api/geocode/json?latlng=%f,%f&sensor=false&language=zh-CN' % (latitude / v, longitude / v)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(), urllib2.HTTPRedirectHandler())

    try:
        str_content = opener.open(url).read()
    except HTTPError, e:
        print 'Error code: ', e.code
        time.sleep(36)
        return get_address()
    except URLError, e:
        print e.reason
        time.sleep(36)
        return get_address()

    if str_content:
        content = json.loads(str_content)
        if content['status'] == 'OK':
            address = content['results'][0]['formatted_address']
            if address.find(' ') > 0:
                address = address[:address.find(' ')]

            address = address.encode('utf-8')
            return (longitude, latitude, address)
        else:
            print content['status'].encode('utf-8') + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            time.sleep(36) # This is due to the 2500/24h limit.
            return get_address()
