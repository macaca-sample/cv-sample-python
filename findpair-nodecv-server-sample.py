#coding:utf-8

import json
import requests

# 

class nodecvSample:

    def __init__(self, host):
        self.host = host

    def getresult(self, files):
        url = self.host + '/opencv/findpairs'
        res = requests.post(url, files=files)
        try:
            jsonres = json.loads(res.text)
            match_res=jsonres["match"]
            if match_res["result"] == True:
                print "Match"
                print 'Screenshot image width: ' + str(match_res["width"])
                print 'Screenshot image height: ' + str(match_res["height"])
                print 'Match rectangle corner1: ('+str(match_res["match_x1"])+','+ str(match_res["match_y1"])+')'
                print 'Match rectangle corner2: ('+str(match_res["match_x2"])+','+ str(match_res["match_y2"])+')'
            else:
                print "Not Match"
        except:
            print "Exception"
        return res.text

if __name__ == '__main__':
    sample = nodecvSample('http://localhost:9900')
    print sample.getresult({
        'image1': ('T-Shirt-logo.jpg', open('./fixture/T-Shirt-logo.jpg', 'rb'), 'image/jpeg', {'Expires': '0'}),
        'image2': ('T-Shirt.jpg', open('./fixture/T-Shirt.jpg', 'rb'), 'image/jpeg', {'Expires': '0'})
    })
