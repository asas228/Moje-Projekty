import pyautogui, time
sila = str(input("Wpisz siłe spamu:  "))


x = "Spam bot"


print(x)

time.sleep(3)
pyautogui.write('Spam Bot Wersja 1.0.6' + " Sila spamu = " + sila)
pyautogui.press('Enter')

sila = int(sila)

time.sleep(1)
y = 10
for x in range(sila):
        pyautogui.press('Enter')
        pyautogui.write('@admin')
        pyautogui.press('Enter')

