def calcular_horas_extras(salario_base, horas):
   return (salario_base * 0.015) * horas

def calcular_descontos_faltas(salario_base, faltas):
    return (salario_base * 0.02) * faltas

def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus == "n" or recebeu_bonus == "N":
        return 0

    if cargo == 1:
        valor = 1000
    elif cargo == 2:
        valor = 500
    elif cargo == 3:
        valor = 300
    elif cargo == 4:
        valor = 100
    return valor

print("* SISTEMA DE FOLHA DE PAGAMENTO *")
nome = input("Nome do funcionário: ")
print("[1] Gerente")
print("[2] Analista")
print("[3] Assistente")
print("[4] Estagiário")
cargo = int(input("Código fo cargo: "))
salario_base = float(input("Salário base: R$ "))
horas_extras = int(input("Total horas extras: "))
faltas = int(input("Total de faltas no mês: "))
recebeu_bonus = input("Bônus por desempenho (S/N): ")

valor_horasextras = calcular_horas_extras(salario_base, horas_extras)
valor_faltas = calcular_descontos_faltas(salario_base, faltas)
valor_bonus = calcular_bonus(cargo, recebeu_bonus)

acrescimos = valor_horasextras + valor_bonus
salario_bruto = salario_base + acrescimos
salario_liquido = salario_bruto - valor_faltas

print("=-"*30)
print(f"HOLERITE DE {nome}")
print("=-"*30)
print("PROVENTOS")
print(f"Salário: R$ {salario_base:.2f}")
print(f"Hora Extra: R$ {valor_horasextras:.2f}")
print(f"Bonus: R$ {valor_bonus:.2f}")
print(f"TOTAL PROVENTOS: R$ {salario_bruto:.2f}")
print("DESCONTOS")
print(f"Faltas: R$ {valor_faltas:.2f}")
print(f"TOTAL DESCONTOS: R$ {valor_faltas:.2f}")
print(f"LÍQUIDO A RECEBER: R$ {salario_liquido:.2f}")