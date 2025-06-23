# 文件名：队列
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append('zhangsan')
print(queue)
queue.popleft()
print(queue)

queue[0] = 'xiongda'    # 并不是支持了随机访问，内部依靠遍历
print(queue)

