choice = 't'

while choice == 't':
    print("Podaj liczbę:")
    
    try:
        liczba = float(input())
        
        for i in range(1, 11):
                print(str(liczba) + " x {0} = ".format(i) + str(liczba * i))
                
    except ValueError:
        print("Nie podałeś liczby!")
        
    print("Czy chcesz podać inną liczbę? (t/n)")
    choice = input()