#Shopping list
shopping=[]
print("What do you want to buy from store?")
print("Type 'DONE' when u complete shopping.")
while True:
    items=input(" ")
    if (items=='DONE'):
        break
    shopping.append(items)
print("This is your items!")
for item in shopping:
    print(item)
