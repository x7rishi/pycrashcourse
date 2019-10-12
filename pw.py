#! /usr/bin/python3
# pw.py -An insecure Password Locker Program
PASSWORD = {'outlook' : 'rishi.iam@live.com','blog' : "sad;fljaweifjsd;lkfj ;sdflk"}
import sys
if (len(sys.argv)<2) :
    print("Usage: python3 pw.py [account] - copy account password")
    sys.exit()
acc_name = sys.argv[1] 


account = sys.argv[2]

if account in PASSWORD :
    print("password is in the database")
else :
    print("password is not found")
