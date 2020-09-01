import os
import sys

try:
    import psutil
    import win32gui
except Exception:
    pass

ENV = os.environ
SYSTEM = os.name
CDIR = sys.argv[0]
PYENV = []
PROCESSES = []


PYINTEPRETATOR = sys.executable

try :
    WINDOWSDIR = ENV['WINDIR']
    LOGFILE = ENV['WINDOWS_TRACING_LOGFILE']
    ROOTDIR = ENV['SYSTEMROOT']
    USERNAME = ENV['USERNAME']
    COMPUTERNAME = ENV['COMPUTERNAME']
    HOMEDIR = ENV['HOMEPATH']
except Exception:
    pass

if ENV['PYTHONPATH']:
    PYTHONPATH = ENV['PYTHONPATH']
elif not ENV['PYTHONPATH']:
    python3 = PYINTEPRETATOR.replace('python.exe', 'Lib')
    PYTHONPATH = python3
else:
    PYTHONPATH = None


windows = ['nt', 'windows', 'win' ,'win32']
unix = ['posix', 'unix', 'linux']

def windows_scan():
    procc_info = {'processor_full' : '', 'kernels' : '', 'cpu_frequency' : ''}
    disks_info = {'disk_usage' : '', 'disk_partition' : ''}
    battery_info = {'battery' : ''}
    if PYTHONPATH is not None:
        pypkg = os.listdir(str(PYTHONPATH))
        for file in pypkg:
            PYENV.append(file)
    else:
        pass
    if psutil:
        procc_info = {'processor_full' : get_cpu_procent(), 'kernels' : get_cpu_count(), 'cpu_frequency' : get_cpu_frequency()}
        battery_info = {'battery' : get_battery()}
        disks_info = {'disk_usage' : get_disk_usage(), 'disk_partition' : get_disks_info()}
        for p in psutil.process_iter():
            PROCESSES.append(p)
    return procc_info, battery_info , disks_info      

def get_cpu_procent(): 
    cpu_procent = psutil.cpu_percent(interval=1)
    CPU_PROCENT = '{}%'.format(cpu_procent)
    return CPU_PROCENT

def get_cpu_count():
    cpu_count = psutil.cpu_count()
    CPU_COUNT = cpu_count
    return CPU_COUNT

def get_cpu_frequency():
    cpu_freq = psutil.cpu_freq()
    CPU_FREQ = "{}-{} ; {}-{}".format("Макс. частота",cpu_freq.max,"Мин. частота", cpu_freq.min)
    return CPU_FREQ

def get_battery():
    battery_level = psutil.sensors_battery()
    if battery_level == None:
        return "нет встроенной батареи"
    battery_level_mins = int(battery_level.secs_left / 60)
    BATTERY = "{}%, {}:{}mins".format(battery_level.percent ,"Времени от батареи", battery_level_mins)
    return BATTERY

def get_disks_info():  
    partitions = psutil.disk_partitions()
    PARTITIONS = []
    for part in partitions:
        PARTITIONS.append(part.device)
    return PARTITIONS

def get_disk_usage():
    memory = psutil.virtual_memory()
    available_in_mb = round(memory.available / 1024)
    total_in_mb = round(memory.total /1024)
    used_in_mb = round(memory.used / 1024 )
    available_in_gb = round(available_in_mb / 1024)
    total_in_gb = round(total_in_mb / 1024)
    used_in_gb = round(used_in_mb /1024)
    MEMORY = "{}:{}GB ; {}:{}GB ; {}:{}GBx".format("Всего памяти", total_in_gb,"Свободно памяти" , available_in_gb, "Занято памяти" , used_in_gb)
    return MEMORY

if SYSTEM in windows:
    print(windows_scan())
    
