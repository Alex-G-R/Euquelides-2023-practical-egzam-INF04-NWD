
a = -1
b = -1

while a <= 0:
    a = int(input("Podaj liczbe A: "))

while b <= 0:   
    b = int(input("Podaj liczbe B: "))

def first():
    global a
    global b
    if a != b:
        if a > b:
            a = a-b
            first()
        else:
            b = b - a
            first()
    else:
        print("Odpowiedz to: ", a)

first()