# redis-rq-docker-compose-demo

Local:
MacBookPro15:redis-rq-demo5 t-saito$ pwd
/Users/t-saito/tmp/redis-rq-demo5

Cf:
https://qiita.com/hoto17296/items/39597f6e26c0186a6e1b
Python で分散タスクキュー (RQ 編)

Usage:

Terminal1>
$ docker-compose up --scale worker=4

Terminal2>
$ docker-compose run --rm worker python app.py 

