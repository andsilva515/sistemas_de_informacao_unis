a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

menor = a

if b < menor:
    menor = b
if c < menor:
    menor = c

print("O menor número é:", min(a, b, c))
