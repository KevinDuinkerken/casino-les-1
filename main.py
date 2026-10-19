PRICE_ENTRY = 10.00
PRICE_DRINK = 4.00
PRICE_GAMBLING_TAX = 2.10

name = input("Wat is je voor- en achternaam: ").title()
birthdate = input("Wat is je geboortedatum? Vul dit in als dd-mm-yyyy: ")
gender = input("Wat is je gender? (m/v/x): ").lower()
initial_budget = float(input("Wat is je startbudget in euro's: "))

last_name = name.split()
total_cost = PRICE_ENTRY + PRICE_DRINK + PRICE_GAMBLING_TAX
balance = initial_budget - total_cost

if gender == "m":
    greeting = ", meneer " + last_name[1]
elif gender == "v":
    greeting = ", mevrouw " + last_name[1]
else:
    greeting = " " + name

if balance > 0:
    entry_balance = "nog genoeg"
else:
    entry_balance = "niet voldoende"

print(f"""
Casino de Gouden Driehoek
-------------------------
Welkom{greeting}

Startbudget:    €{initial_budget:.2f}
Vaste kosten:   €{total_cost:.2f}
Saldo:          €{balance:.2f}

Je hebt {entry_balance} budget voor toegang tot het casino""")
