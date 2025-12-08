# Lê a idade em dias
idade_dias = int(input("Digite sua idade em dias: "))

# Cálculo (considerando 1 ano = 365 dias e 1 mês = 30 dias)
anos = idade_dias // 365
resto = idade_dias % 365
meses = resto // 30
dias = resto % 30

# Exibe o resultado
print(f"{anos} ano(s), {meses} mês(es) e {dias} dia(s).")
