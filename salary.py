#Clean the messy salary
salary='$867,001'.split('$')
a="".join(salary)
b=a.split(',')
c="".join(b)
print(c)
