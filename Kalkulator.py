#simple calculator program
print("Kalkulator w wersji Python")
print("Wybierz + dla dodawania")
print("Wybierz - dla odejmowania")
print("Wybierz * dla mnożenia")
print("Wybierz : dla dzielenia")
print("Wybierz ^ dla potęgowania")
print("Wybierz R dla reszty z dzielenia")
print("Wybierz _ dla dzielenia z wynikiem zaokrąglonym w dół")
print("Wybierz ! dla działania silnia")
print("Wybierz X dla zakończenia działania")

choice = input()
if choice == '!':
    result = 1
    factorial = int(input("podaj liczbę do wykonania silni: "))
    while (factorial > 1):
        result *= factorial
        factorial -= 1
    print("Wynik =", result)
else:
    result = float(input("Podaj pierwszą liczbę: "))
    while choice == '+' or '-' or '*' or ':' or '^' or 'R' or '_' or 'X':
        if (choice == 'X'):
            print ("Wynik =", result)
            break
        else:
            print("Podaj liczbę do działania", choice)
            Number = float(input())
            if (choice == '+'):
                result += Number
                choice = input("Podaj kolejne działanie")
            elif (choice == '-'):
                result -= Number
                choice = input("Podaj kolejne działanie")
            elif (choice == '*'):
                result *= Number
                choice = input("Podaj kolejne działanie")
            elif (choice == ':' and Number != 0):
                result /= Number
                choice = input("Podaj kolejne działanie")
            elif (choice == ':' and Number == 0):
                print("działanie niepoprawne")
                choice = input("Podaj kolejne działanie")
            elif (choice == '^'):
                result **= Number
                choice = input("Podaj kolejne działanie")
            elif (choice == 'R'):
                result %= Number
                choice = input("Podaj kolejne działanie")
            elif (choice == '_' and Number != 0):
                result //= Number
                choice = input("Podaj kolejne działanie")
            elif (choice == '_' and Number == 0):
                print("działanie niepoprawne")
                choice = input("Podaj kolejne działanie")    
            else:
                print("Niepoprawny wybór!")
