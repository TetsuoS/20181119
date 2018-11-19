import os
from time import sleep
import redis
from rq import Queue
from tasks import add

q = Queue(connection=redis.from_url(os.environ.get('RQ_REDIS_URL')))

tasks = [q.enqueue(add, args=(i, 1)) for i in range(10)]

sleep(1)

print([task.result for task in tasks])
