import os
import time
class Logger():
    def __init__(self, path = 'defaultLog.txt'):
        self.path = path
        #if file doesn't exist, create it
        if not os.path.exists(self.path):
            #create it
            with open(self.path, 'w') as F:
                ...
                pass
    def logRow(self,message):
        now = time.ctime(time.time())
        with open(self.path, 'a') as F:
            F.write(f"{now}, {message}\n")
