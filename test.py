import os

cmdstr='cmd.exe'
print(os.popen(cmdstr).encode('utf8'))
print(os.popen(cmdstr))