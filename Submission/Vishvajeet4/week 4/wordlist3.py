import zipfile
import time

def main():
    try:
        Zip = raw_input(" Zip File Name: ")
        myZip = zipfile.ZipFile(Zip)
    except zipfile.BadZipfile:
        print "[!]  error opening your zip file."
        return

    password = ''
    
    start = time.time()
    pwdfile = raw_input("  wordlist dictionary path: ")
    try:
        f = open(pwdfile,"r")
    except:
        print "\nFile not found"
        quit()
    passes = f.readlines()
    for pass_count, x in enumerate(passes):
        password = x.strip()
        try:
            myZip.extractall(pwd = password)
            end = time.time()
            t_time = end - start
            
            print "\nPassword cracked: %s\n" % password
            print "Total runtime was -- ", t_time, "second"
            time.sleep(10)
            return
        except Exception as e:
            if str(e[0]) == 'Bad password for file':
                pass 
            elif 'Error -3 while decompressing' in str(e[0]):
                pass 
            else:
                print e
    print " Your password not found."

if __name__ == '__main__':
 main()