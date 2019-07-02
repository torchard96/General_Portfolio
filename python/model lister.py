from os import listdir,walk
from os.path import isfile,join
dir = 'enter gamedata directory'

f=[]

for subdir, dirs, files in walk(dir):
    for file in files:
        if file.endswith('.mu'):
            f.append(join(subdir,file.replace('.mu','')))
        
f2=[]
for file in f:
    f2.append(file.replace(dir+'\\',''))

for file in f2:
    print('model = '+file)
