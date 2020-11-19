#Ride Cost Calculator
distance = float(input("Enter distance in kilometres: "))
litresPer100K = float(input("Enter fuel average (ltr/100km): "))
pricePerLitre = float(input("Enter diesel price perlitre ($): "))
cost = distance / 100 * litresPer100K * pricePerLitre
print (cost)