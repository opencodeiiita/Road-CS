#you to download "rockyou.txt".
#url="https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"


from zipfile import ZipFile
import sys

filename=input("input file name: ")

fh = open('rockyou.txt', encoding='utf-8', errors='ignore')

x=1
while x==1:
    line = fh.readline()
    #sys.exit()
    #preg_replace("/\r|\n/", "",line);
    line.strip("\n")
    k=line
    k = k.replace("\r", "")
    k = k.replace("\n", "")
    #print(k)
    #sys.exit()
    #print(line)
    with ZipFile(filename, 'r') as zip:
        try:
            zip.extractall(pwd=bytes(k, 'utf-8'))
            print('Done!')
            x=-1
        except:
            pass
    print(line)
    if not line:
        break
fh.close()
