import math

# Leitura dos valores
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Coloca os valores em ordem para facilitar a verificação
lado_maior = max(a, b, c)

# Verifica se podem formar triângulo
if a < b + c and b < a + c and c < a + b:
    print("\nOs valores formam um triângulo!")

    # Cálculo da área usando a fórmula de Heron
    p = (a + b + c) / 2   # semiperímetro
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    print(f"Área do triângulo = {area:.2f}")
else:
    print("\nOs valores NÃO formam um triângulo.")
    print(f"Valores lidos: {a}, {b}, {c}")


"""
Exemplos de Testes

Exemplo 1 — Forma triângulo

Entrada:
a = 3
b = 4
c = 5

Saída:
Os valores formam um triângulo!
Área do triângulo = 6.00

Exemplo 2 — NÃO forma triângulo
Entrada:
a = 10
b = 3
c = 4

Saída:
Os valores NÃO formam um triângulo.
Valores lidos: 10, 3, 4

Motivo: 10 > 3 + 4 → impossível formar triângulo.

Exemplo 3 — Forma triângulo

Entrada:
a = 7
b = 8
c = 5

Saída:
Os valores formam um triângulo!
Área do triângulo = 17.32

Exemplo 4 — NÃO forma triângulo

Entrada:
a = 15
b = 7
c = 3

Saída:
Os valores NÃO formam um triângulo.
Valores lidos: 15, 7, 3


"""