def delta(a, b, c):
    delta = 0
    delta = b*b - 4 * a * c
    return delta

def x1(a, b, c):
    x1 = 0
    x1 = (-b + delta(a, b, c)**0.5)/2*a
    return x1

def x2(a, b, c):
    x2 = 0
    x2 = (-b - delta(a, b, c)**0.5)/2*a
    return x2

def x0(a, b, c):
    x0 = 0
    x0 = -b / 2*a
    return x0

print("Witaj w programie do znajdowania miejsc zerowych trójmianu kwadratowego")

choice = 't'

while choice == 't':
    
    try:
        a, b, c = map(float, input("Podaj współczynniki trójmianu w kolejności a, b, c odzielając je spacją:\n").split())

        print("Delta tego trójmianu wynosi: "+ str(delta(a, b, c)))
    
        if delta(a, b, c) < 0:
            print("Delta jest ujemna, więc podany trójmian kwadratowy nie ma rozwiązań w zbiorze liczb rzeczywistych")
            
        elif delta(a, b, c) == 0:
            print("Delta wynosi zero, więc podany trójmian kwadratowy ma jedno rozwiązanie\n Liczbę "+ str(x0(a, b, c)))

        else:
            print("Delta jest większa od zera, więc rozwiązaniami podanego trójmianu kwadratowego są liczby:\n" + str(x1(a, b, c)) + " oraz " + str(x2(a, b, c)))
    
    except ValueError:
        print("Nie podałeś poprawnych współczynników!")

    choice = input("Czy chcesz sprawdzić inny trójmian kwadratowy? (t/n)")
