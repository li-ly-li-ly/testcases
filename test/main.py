import time
import logging
import threading
logging.basicConfig(level=logging.INFO)
nloops=[2,4]
loops = len(nloops)
class MyThread (threading.Thread):
    def __init__(self,func,args,name=''):
        self.func =func
        self.args=args
        self.name =name
    def fun(self):
        self.func(*self.args)
def loop(nloop,nsec):
    logging.info("start loop" + str(nloop)+"  at "+time.ctime())
    time.sleep(nsec)
    logging.info("end loop" + str(nloop)+"  at "+time.ctime())

def main():
    logging.info("loop main start" +time.ctime())
    threads = []
    for i in range(loops):
        t = threading.Thread(target=loop,args=(i,nloops[i]))
        threads.append(t)
    for i in range(loops):
        threads[i].start()
        threads[i].join()
    for i in range(loops):
        threads[i].join()
    logging.info("loop main stop" + time.ctime())
if __name__ == '__main__':
    main()
