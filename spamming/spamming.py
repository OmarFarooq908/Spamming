import pyautogui

print(" ______________________________________________________________ ")
print("|                                                              |")
print("| In the Name of God, the Most Gracious and the Most Merciful. |")
print("|______________________________________________________________|")
print(" ________________________________ ")
print("|                                |")
print("| Name   :  Muhammad Omar Farooq |")
print("| Roll No:  20-CP-33             |")
print("|________________________________|")
print("")

x = input(" >> Type the string that you want to spam >>  ")
while True:
    try:
        print("")
        print(" | WARNING! Once you enter the number of spams you want to send, the program won't end until the program is forced to terminate |")
        y = int(input(" >> Type the number of spams you want to send in one session >>  "))
        print("")
    except ValueError:
        print(" Please enter a positve integer. ")
        continue
    else:
        if y <=0:
            print("Please enter a positive integer.")
        else:
            break

while True:
    try:
        print("")
        print(" | WARNING! Once you enter the number of spams you want to send, the program won't end until the program is forced to terminate |")
        print(" | The interval should be a positive number ")
        z = float(int(input(" >> Type the intereval between each spam message >>  ")))
    except ValueError:
        print(" Please enter a positve integer. ")
        continue
    else:
        if z <0:
            print("Please enter a positive integer.")
        else:
            break
i=0

while i<y:
    pyautogui.write(x)
    pyautogui.press('enter',interval=z)
    i += 1
