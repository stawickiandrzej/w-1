choice = 't'

print("Witaj w programie do sprawdzania znaku liczby")

while choice == 't':

    try:
            liczba = float(input("Podaj liczbę:"))
            if liczba > 0:
                print("Liczba jest dodatnia")
                
            elif liczba < 0:
                print("Liczba jest ujemna")
            
            else:
                print("Liczba jest zerem")
    except ValueError:
        print("Nie podałeś liczby!")

    choice = input("Czy chcesz podać inną liczbę? (t/n)")
