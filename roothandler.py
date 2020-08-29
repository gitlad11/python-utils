import os 
import shutil

path = os.getcwd()

ACCESS = os.access(r'cleaner.py', os.W_OK)
print(ACCESS)

if ACCESS == True:
    os.chmod(r'cleaner.py' , 777)


