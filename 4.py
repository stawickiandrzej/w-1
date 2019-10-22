choice = 't'
skala = 'g'

def KtoM(liczba):
    KtoM = 0
    KtoM = liczba * 0.621371
    return KtoM

def MtoK(liczba):
    MtoK = 0
    MtoK = liczba * 1.60934
    return MtoK

print("Witaj w programie do konwersji odległości!")

while choice == 't':
    
    skala = input("W jakich jednostkach chcesz wpisać odległość?\n Wpisz k dla kilometrów lub m dla mil...")

    if skala == 'k':
       # print("Podaj liczbę kilometrów:")
        try:
            liczba = float(input("Podaj liczbę kilometrów:"))
            print(str(liczba) +" kilometrów to "+ str(KtoM(liczba)) +" mil")
                
        except ValueError:
            print("Nie podałeś liczby!")
    elif skala == 'm':
       # print("Podaj liczbę mil:")
        try:
            liczba = float(input("Podaj liczbę mil:"))
            print(str(liczba) +" mil "+ str(MtoK(liczba)) +" kilometrów")
                
        except ValueError:
            print("Nie podałeś liczby!")
    else:
        print("Zły wybór!")

    choice = input("Czy chcesz podać inną liczbę? (t/n)")
