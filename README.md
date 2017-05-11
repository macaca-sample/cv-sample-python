# cv-sample-python

## Installation
``` bash
$ pip install -r requirements.txt
```

## Run

``` bash
# basic example
$ python opencv-sample.py

# after start nodecv server

# dissimilarity example
$ python nodecv-server-sample.py

# find pairs example
$ python findpair-nodecv-server-sample.py

# if you prefer using your own post curl command for 'find pairs'
curl -i -X POST \
  -H "Content-Type: multipart/form-data" \
  -F "image1=@./fixture/T-shirt-logo.jpg" \
  -F "image2=@./fixture/T-shirt.jpg" \
  http://localhost:9900/opencv/findpairs
```



## License

The MIT License (MIT)
