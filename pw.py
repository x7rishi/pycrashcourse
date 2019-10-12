#! /usr/bin/python3
# pw.py -An insecure Password Locker Program

PASSWORD = {'outlook' : 'rishi.iam@live.com','blog' : "sad;fljaweifjsd;lkfj ;sdflk"}
import sys
import pyperclip as pc
if (len(sys.argv)<2) :
    print("Usage: python3 pw.py [account] - copy account password")
    sys.exit()
acc_name = sys.argv[1] 


account = sys.argv[2]

if account in PASSWORD :
    print("password is in the database")
    pc.copy(PASSWORD[account])
    print("Password for %s is copied to clipboard"%account)
    
else :
    print("password is not found")
