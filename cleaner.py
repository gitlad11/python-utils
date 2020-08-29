import os 
import sys
from datetime import datetime, timedelta

CPATH = os.getcwd()
ENV = os.environ
SYSTEM = os.name
proccessId = os.getpid()
try:
    HOME = ENV['HOME']
except Exception:
    HOME = ENV['HOMEPATH']
finally:
    pass


CDIR = os.listdir(CPATH)
LOGFILE = 'logpy.txt'
for d in CDIR:
    print(d)
if LOGFILE in CDIR:
    pass
else:
    with open(LOGFILE, 'w', encoding='utf-8') as file:
       pass



#for c in ENV:
    #print(c)
print(ENV['TMP'])

os.chdir(ENV['TEMP'])

temp = os.listdir()
winLog = ENV['WINDOWS_TRACING_LOGFILE']

today = datetime.today()
print(today)

yesterday =  datetime.now() - timedelta(days=1)
print(yesterday)

print('-----------------------------------------')


for f in temp:
    time = datetime.fromtimestamp(os.stat(f).st_mtime)
    print(time)
    size = int(os.stat(f).st_size)
    print(size)
    if size > 3000 and time < yesterday:
        with open(LOGFILE, 'w') as file:
            file.write(str(f) + '\n')        
            os.remove(f)
            
            
            
            
   
 



