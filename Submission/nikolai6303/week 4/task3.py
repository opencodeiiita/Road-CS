#you to download "rockyou.txt".
#url="https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"


from zipfile import ZipFile
import sys

file=input("input file name: ")

fh = open('rockyou.txt')
while True:
    line = fh.readline()
    with ZipFile(file, 'r') as zip:
        try:
            with ZipFile(filename, 'r') as zip:
                zip.extractall(pwd=bytes(result, 'utf-8'))
                print('Done!')
                sys.exit()
        except:
            pass
    #print(line)
    if not line:
        break
fh.close()
