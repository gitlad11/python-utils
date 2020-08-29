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

print('CLEAR TEMPORARY FILES')
print('----------------------------------------------------------------')
for f in temp:
    time = datetime.fromtimestamp(os.stat(f).st_mtime)
    print(time)
    size = int(os.stat(f).st_size)
    print(size)
    if size > 3000 and time < yesterday:
        with open(LOGFILE, 'w') as file:
            file.write(str(f) + '\n')        
            os.remove(f)
            

localdata = ENV['LOCALAPPDATA']       
appdata = ENV['APPDATA']            

print("CLEAR CACHE")
print("----------------------------------------------------------------")
def cachehandler(datapath):
    CACHES = ['CACHE', 'cache', 'TEMP', 'temporary', 'log', 'cookie']

    for fullpath, dirs, files in os.walk(datapath, topdown=False):
        for dir in dirs:
            for ca in CACHES:
                if ca in dir:
                    print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
                    print('directory: ' + dir)
                    print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
                    os.chdir('{}/{}/'.format(fullpath,dir))
                    dirfiles = os.listdir()
                    for df in dirfiles:
                        if df.endswith('.txt'):
                            os.remove(df)
                            print(df + ' - txtfile has been deleted')
                        if df.endswith('.log'):
                            os.remove(df)
                            print(df + ' - logfile has been deleted')
                        else:
                            print(df + ' - is not txt, log')
cachehandler(localdata)
