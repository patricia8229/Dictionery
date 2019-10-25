from CLASSES.ATM import ATMCard
martinCard  = ATMCard(1000)
LucyCard = ATMCard()
LetinaCard  = ATMCard()

#print (type(martinCard))
print (LucyCard.colour)
LetinaCard.deposit(100)
print(LetinaCard.balance)
print(LucyCard.balance)
LucyCard.withdraw(1000)