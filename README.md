# cv-sample-python

## Installation

```bash
$ pip install -r requirements.txt
```

## Run

```bash
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

```bash
$ npm i git-contributor -g
$ git-contributor
```
<!-- GITCONTRIBUTOR_START -->

## Contributors

|[<img src="https://avatars.githubusercontent.com/u/1011681?v=4" width="100px;"/><br/><sub><b>xudafeng</b></sub>](https://github.com/xudafeng)<br/>|[<img src="https://avatars.githubusercontent.com/u/870082?v=4" width="100px;"/><br/><sub><b>Chenxin</b></sub>](https://github.com/Chenxin)<br/>|[<img src="https://avatars.githubusercontent.com/u/356347?v=4" width="100px;"/><br/><sub><b>liangjun-jiang</b></sub>](https://github.com/liangjun-jiang)<br/>|
| :---: | :---: | :---: |


This project follows the git-contributor [spec](https://github.com/xudafeng/git-contributor), auto updated at `Thu Nov 18 2021 01:01:06 GMT+0800`.

<!-- GITCONTRIBUTOR_END -->

## License

The MIT License (MIT)
