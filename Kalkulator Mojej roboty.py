
def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnożnie(x, y):
    return x * y

def dzielenie(x, y):
    return x / y

print("Wybierz dzialanie")
print("1 = dodawanie")
print("2 = odejmowanie")
print("3 = mnożenie")
print("4 = dzielenie")
print("5 = wyjście")

wybór = input("wybierz liczbę od 1 do 5 :    ")


if wybór == "5":
    print("|")


elif wybór == "1":
    x = float(input("Wprowadź liczbę X:   "))
    y = float(input("Wprowadź liczbę Y:   "))
    print(x, "+", y ,"=", dodawanie(x, y))

elif wybór == "2":
    x = float(input("Wprowadź liczbę X:   "))
    y = float(input("Wprowadź liczbę Y:   "))
    print(x, "-", y ,"=", odejmowanie(x, y))

elif wybór == "3":
    x = float(input("Wprowadź liczbę X:   "))
    y = float(input("Wprowadź liczbę Y:   "))
    print(x, "*", y ,"=", mnożnie(x, y))

elif wybór == "4":
    x = float(input("Wprowadź liczbę X:   "))
    y = float(input("Wprowadź liczbę Y:   "))
    print(x, ":", y ,"=", dzielenie(x, y))

else:
    print("źle wybrałeś")





print("\n" * 100)

print("KONIEC PROGRAMU")

print("Autor : Krzysztof Michałczak")
