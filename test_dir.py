import os
import time
print(os.path.exists('b'))
if not os.path.exists('b'):
    os.mkdir('b')
if not os.path.exists('b/test.txt'):
    f = open('b/test.txt','w')
    f.write('hssds')
    f.close()
print(time.asctime())
print(time.time())
print(time.localtime())
print(time.strftime('%Y-%m-%d %H-%M-%S',time.localtime()))
now_time = time.time()
aj_time = now_time - 2*24*60*60
print(time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(aj_time)))

