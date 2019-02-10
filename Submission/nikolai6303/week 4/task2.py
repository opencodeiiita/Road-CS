

from zipfile import ZipFile

from sys import exit


file=input("input file name: ")
length=int(input("Enter the maximum of characters: "))


filename=file;


lista=[0 for x in range(length)]
x=length-1
string="abcdefghijklnmopqrstuvwxyz1234567890"
while(x>-1):
    result = ""
    if lista[x] == len(string) - 1:
        for z in range(length):
            result += string[lista[z]]
        lista[x] = 0
        x -= 1
    elif x == length - 1:
        for z in range(length):
            result += string[lista[z]]
        lista[x] += 1
    else:
        for z in range(length):
            result += string[lista[z]]
        lista[x] += 1
        if x > 0:
            x += 1
        else:
            x = length - 1

    print(result)
    with ZipFile(filename, 'r') as zip:
        try:
            with ZipFile(filename, 'r') as zip:
            # print("extracting files now")
             zip.extractall(pwd=bytes(result, 'utf-8'))
             print('Done!')
             #exit()
             x=-1
        except:
            pass
   

