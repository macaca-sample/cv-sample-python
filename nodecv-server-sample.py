#coding:utf-8

import json
import requests

# 

class nodecvSample:

    def __init__(self, host):
        self.host = host

    def getresult(self, files):
        url = self.host + '/opencv/dissimilarity'
        res = requests.post(url, files=files)
        return json.loads(res.text)['dissimilarity']

if __name__ == '__main__':
    sample = nodecvSample('http://localhost:9900')
    print sample.getresult({
        'image1': ('T-Shirt-logo.jpg', open('./fixture/T-Shirt.jpg', 'rb'), 'image/jpeg', {'Expires': '0'}),
        'image2': ('T-Shirt.jpg', open('./fixture/T-Shirt-logo.jpg', 'rb'), 'image/jpeg', {'Expires': '0'})
    })
