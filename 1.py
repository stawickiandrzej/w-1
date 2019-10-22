choice = 't'

while choice == 't':
    print("Podaj liczbę całkowitą dla której mają być znalezione wszystkie dzielniki: ")
    
    try:
        liczba = abs(int(input()))
        if liczba == 0:
            print("Zero ma nieskończenie wiele dzielników poza zerem")
        else:
            for i in range(1, liczba + 1):
                if liczba % i == 0:
                    print(i)
                    
    except ValueError:
        print("Nie podałeś liczby całkowitej!")

    choice = input("Czy chcesz podać inną liczbę? (t/n)")
