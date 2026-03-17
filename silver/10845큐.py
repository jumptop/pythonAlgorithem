import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()
# queue.appendleft(0)

for i in range(N):
    command = input().split()
    cmd = command[0]

    if cmd == 'push':
        queue.append(int(command[1]))
    elif cmd == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif cmd == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)