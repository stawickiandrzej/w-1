choice = 't'
skala = 'g'

def CtoF(liczba):
    CtoF = 0
    CtoF = (liczba*9/5)+32
    return CtoF

def FtoC(liczba):
    FtoC = 0
    FtoC = (liczba-32)*(5/9)
    return FtoC

print("Witaj w programie do konwersji temperatur!".)

while choice == 't':
    
    skala = input("W jakich jednostkach chcesz wpisać wartość temperatury?\n Wpisz c dla skali Celsjusza lub f dla skali Fahrenheita...")

    if skala == 'c':
        print("Podaj stopnie Celsjusza:")
        try:
            liczba = float(input())
            print(str(liczba) +" stopni Celsjusza to "+ str(CtoF(liczba)) +" stopni w skali Fahrenheita")
                
        except ValueError:
            print("Nie podałeś liczby!")
    elif skala == 'f':
        print("Podaj stopnie Fahrenheita:")
        try:
            liczba = float(input())
            print(str(liczba) +" stopni Celsjusza to "+ str(FtoC(liczba)) +" stopni w skali Fahrenheita")
                
        except ValueError:
            print("Nie podałeś liczby!")
    else:
        print("Zły wybór!")

    choice = input("Czy chcesz podać inną liczbę? (t/n)")
