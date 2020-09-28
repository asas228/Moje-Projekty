Loop = 1
print("\n" * 1)
print("Kalkulator")


def dodawanie(x, z):
   return x + z

def odejmowanie(x, z):
    return x - z

def mnożenie(x, z):
    return x * z

def dzielenie(x, z):
    return x / y

if Loop == 1:
    while Loop ==1:
        print("\n" * 1)
        x = float(input("Wpisz liczbe:   "))
        y = input("wpisz znak matematyczny( + , - , * , / ,):  ")
        z = float(input("Wpisz drugą liczbe:   "))

        if y == "+":
            print(x , "+" , z , "=" , dodawanie(x, z))

        if y == "-":
            print(x, "-", z, "=" , odejmowanie(x, z))

        if y == "*":
            print(x, "*", z, "=" , mnożenie(x, z))

        if y == "/":
            print(x, "/", z , "=", dzielenie(x, z))