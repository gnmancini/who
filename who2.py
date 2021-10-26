import os
import time

def chequeo():
    loop = True
    while (loop):  
        result = os.popen('w | tail -n +3 | wc -l').read()
        #print(result)
        if int(result) > 1 :
            print(result)
        time.sleep(60)

chequeo()