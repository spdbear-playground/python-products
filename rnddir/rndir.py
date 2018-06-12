import os
import random
import subprocess

path = os.getcwd()
dirs = []

for x in os.listdir(path):  
    if os.path.isdir(path + '\\' +  x):  #パスに取り出したオブジェクトを足してフルパスに
        dirs.append(x)

print(dirs)
random.shuffle(dirs)

ans = random.choice(dirs)
anspath = path + '\\' + ans
print(ans)
subprocess.Popen(['explorer', anspath])