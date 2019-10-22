from fractions import Fraction

print("Witaj w programie do dodawania ułamków zwykłych")

choice = 't'

while choice == 't':
    
    try:
        a, b = map(int, input("Podaj pierwszy ułamkek zwykły ze slashem ""/"" zamiast kreski ułamkowej:\n").split("/"))
        
        if b == 0:
            print("Nie dziel przez 0!")
            break
        
        else:
            frac1 = Fraction(a, b)
        
    except ValueError:
        print("Nie podałeś poprawnych wartości!")

    try:
        c, d = map(int, input("Podaj drugi ułamkek zwykły ze slashem ""/"" zamiast kreski ułamkowej:\n").split("/"))
        
        if d == 0:
            print("Nie dziel przez 0!")
            break
        
        else:
            frac2 = Fraction(c, d)
        
    except ValueError:
        print("Nie podałeś poprawnych wartości!")
    
    
    try:
        frac = 0
        frac = frac1 + frac2
        print("Suma podanych ułamków zwykłych wynosi: "+ str(frac))
        
    except NameError:
        print("Nie podałeś jednego z ułamków!")

    choice = input("Czy chcesz dodać inne ułamki? (t/n)")
