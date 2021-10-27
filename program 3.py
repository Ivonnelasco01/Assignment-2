money = int(input("How much is your money?"))
apple = int(input("How much is the price of 1 apple?"))

quantity = money // apple
total = quantity * apple
change = money - total

print(f"You can buy {quantity} apples and your change is {change} pesos.")