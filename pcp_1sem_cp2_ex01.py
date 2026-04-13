cod_origem = int(input("Código do Estado de origem da carga (1-5): "))
peso = float(input("Peso da carga em toneladas: "))
cod_carga = int(input("Código da carga (10-40): "))

peso_kg = peso * 1000

print("=-"*20)

print(f"Peso da carga: {peso_kg} Kg")

preco_carga = 0

if 10 < cod_carga < 20:
    preco_carga = peso_kg * 100
else:
    if 21 < cod_carga < 30:
        preco_carga = peso_kg * 250
    else:
        if 31 < cod_carga < 40:
            preco_carga = peso_kg * 340

print(f"Preço bruto da carga: R$ {preco_carga:.2f}")

print("=-"*20)

if cod_origem == 1:
    print("DESCONTOS DO ESTADO 1:")
    print(f"Imposto: R$ {preco_carga*0.35}")
    print(f"Valor total transportado: R$ {preco_carga + (preco_carga*0.35)}")
else:
    if cod_origem == 2:
        print("DESCONTOS DO ESTADO 2:")
        print(f"Imposto: R$ {preco_carga * 0.25}")
        print(f"Valor total transportado: R$ {preco_carga + (preco_carga * 0.25)}")
    else:
        if cod_origem == 3:
            print("DESCONTOS DO ESTADO 3:")
            print(f"Imposto: R$ {preco_carga * 0.15}")
            print(f"Valor total transportado: R$ {preco_carga + (preco_carga * 0.15)}")
        else:
            if cod_origem == 4:
                print("DESCONTOS DO ESTADO 4:")
                print(f"Imposto: R$ {preco_carga * 0.05}")
                print(f"Valor total transportado: R$ {preco_carga + (preco_carga * 0.05)}")
            else:
                if cod_origem == 5:
                    print("DESCONTOS DO ESTADO 5:")
                    print(f"* ESTADO ISENTO DE IMPOSTO *")
                    print(f"Valor total transportado: R$ {preco_carga}")
