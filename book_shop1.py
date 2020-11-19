orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95],
      ["98762", "Programming Python, Mark Lutz", 5, 56.80],
      ["77226", "Head First Python, Paul Barry", 3,32.95],
      ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
    ]
#print(orders)
happy=[]
for order in orders:
    Num = int(order[0])
    quantity = order[2]
    price = order[3]
    total=quantity * price
    if total<=100:
        total = total+10
    else:
        total
    happy.append((Num,round(total,2)))
    print(happy)
