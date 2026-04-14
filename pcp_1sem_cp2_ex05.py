def pode_aprovar(idade, renda, valor):
    if idade >= 18 and valor <= (renda * 20):
        return True
    else:
        return False

def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    if 7 <= parcelas <= 12:
        return 0.08
    if 13 <= parcelas <= 24:
        return 0.1

def calcular_parcela(valor, taxa, parcelas):
    cima = taxa * (1 + taxa)**parcelas
    baixo = (1 + taxa)**parcelas - 1
    pmt = valor * (cima / baixo)
    return pmt

def calcular_total(parcela, parcelas):
    return parcela * parcelas

def calcular_juros(total, valor):
    return total - valor

nome = input("Nome: ")
idade = int(input("Idade: "))
renda_mensal = float(input("Renda mensal: R$ "))
valor_solicitado = float(input("Valor do empréstimo: R$ "))
numero_parcelas = int(input("Quantiadde de parcelas (3-24): "))

if pode_aprovar(idade, renda_mensal, valor_solicitado):
    valor_taxa = definir_taxa(numero_parcelas)
    valor_parcelas = calcular_parcela(valor_solicitado, valor_taxa, numero_parcelas)
    valor_total = calcular_total(valor_parcelas, numero_parcelas)
    total_juros = calcular_juros(valor_total, valor_solicitado)
    print("=-"*30)
    print("FINANCIAMENTO APROVADO!")
    print(f"Cliente: {nome}")
    print(f"Valor financiado: {valor_solicitado:.2f}")
    print(f"Taxa de juros aplicada: {valor_taxa * 100:.0f}% ao mês")
    print(f"Parcelas: {numero_parcelas}x de R$ {valor_parcelas:.2f}")
    print(f"Valor total a pagar: R$ {valor_total:.2f}")
    print(f"Total de Juros: R$ {total_juros:.2f}")
else:
    print("=-"*30)
    print("FINANCIAMENTO NEGADO!")
    print(f"Sua idade e/ou renda são insuficientes para aprovação da solicitação.")