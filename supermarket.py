lib={}
while True:
    anna=input("Enter item with price : ")
    if not anna:
        break
    list=anna.split()
    price=list[1]
    item=" ".join(list[:1])
    lib[item]=lib.get(item,0)+int(price)
for chat,kara in lib.items():
    print(chat,kara)
