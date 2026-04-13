lado = []
lado.append(float(input("Primeiro lado: ")))
lado.append(float(input("Segundo lado: ")))
lado.append(float(input("Terceiro lado: ")))

lado.sort(reverse=True)

A = lado[0]
B = lado[1]
C = lado[2]

if A >= (B + C):
    print("NÃO FORMA TRIANGULO")
else:
    if A**2 == (B**2 + C**2):
        print("TRIANGULO RETANGULO")
    else:
        if A**2 > (B**2 + C**2):
            print("TRIANGULO OBTUSANGULO")
        else:
            if A**2 < (B**2 + C++2):
                print("TRIANGULO ACUTANGULO")
            else:
                if A == B == C:
                    print("TRIANGULO EQUILATERO")
                else:
                    if A == B or A == C or B == C:
                        print(" TRIANGULO ISOSCELES")