while (True):
    str1=input("Enter the age: ")
    if not str1:
        break
    if (int(str1) >0 and int(str1) <=1):
        print ("Infant")
    elif (int(str1) >=1 and int(str1) < 18):
        print("Child")
    elif (int(str1) >=18 and int(str1) <= 60):
        print("Adult")
    else:
        print ("Senior citizen")






