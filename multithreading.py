import time
import threading

def f1():
    for i in range(1,11,1):
        print(i)
        time.sleep(1)

def f2():
    for b in range(1, 16,1):
        print("      Dillan")
        time.sleep(1)


thread1 = threading.Thread(target = f1)
thread2 = threading.Thread(target = f2)
thread1.start()
thread2.start()