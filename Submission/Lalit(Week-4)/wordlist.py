import zipfile 
import sys
from optparse import OptionParser
dictionary_mode = False
force_mode = False
force_num = False
force_EN = False
force_en = False
def main():
    global ans
    global path
    global dictionary_mode
    global dict_path
    ans = False
    #Define parameter 
    #Comment part line 29-45 is first coding for process sys.argv after i find simple function : optparse to define my parameter 
    parser = OptionParser("useage: %prog"+"-u <Zip file path> -D <Dictionary Path>")
    parser.add_option('-u',dest='zip_name',type='string',help='Zip file path')
    parser.add_option('-D',dest='dict_name',type='string',help='Dictionary file path')
    (options,args) = parser.parse_args()
    #To find parameter hava value or not
    if (options.zip_name==None)or(options.dict_name==None):
        print parse.useage
        exit(0)
    else:
        dictionary_mode = True
        dict_path = options.dict_name
        path = options.zip_name
        #This old code for porcess parameter
        #old code
        #This is to check parameter is compelete or not if true do function
    if dictionary_mode == True:
        dictmode(dictionary_mode,path,dict_path)
    #print ans
    #ans is falce that say the Dictionary.txt doesnt find password for Your.zip
    if ans is False:
        print "So sad !!!"
    #This function is read .txt line by line and throw line(passwd) tk extract function to Try password
def dictmode(dictbool,zippath,dictpath):
    #global ans
    with open(dictpath,'r') as f:
        for line in f.readlines():
            passwd = line.strip('\n')
            #ans = extractFile(zippath,passwd)
            extractFile(zippath,passwd)
    #This function is to test zip I use try except to skip error password!!
def extractFile(zippath,password):
    zip_file = zipfile.ZipFile(zippath)
    global ans
    try:
        zip_file.extractall(pwd=password)
        print 'Zip crack successful!!! Password is :' + password
        ans = True
        return password
    except:
        #ans = 'No Passwd'
        return
if __name__ == '__main__':
    main()