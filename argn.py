import sys
print("Length of the argument ",len(sys.argv))
print("name of the file is ",sys.argv[0])
print("Argument is : ",str(sys.argv))
if (sys.argv[1] == 'rishi'):
    print("Hello, Rishi How are you !")
else :
    print("Who the hell you are.")

if ((sys.argv[2]).isdigit()):
    print("Your age is %s"%sys.argv[2])

    