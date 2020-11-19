salary = ['$876,001','$543,903','$2453,896']
list3 = []
for item in salary:
    list1=item.split(",")
    str1 = "".join(list1)
    list2 = str1.split("$")
    str2 = "".join(list2)
    str2 = int(str2)
    list3.append(str2)
print(list3)