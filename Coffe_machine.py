import time

print("Welcome to the coffee machine! enter £2.25")
money = input()
money = float(money)
if money < 2.25:
    change = 2.25-money
    print(f"Not enough money, you need £{change: .2f} more")
elif money >= 2.25:
    print("Making the coffee...")
    time.sleep(2)
    print("here is your coffe, enjoy!")
    change = money - 2.25
    if change > 0:
        print(f"here's your change : £{change: .2f}")
