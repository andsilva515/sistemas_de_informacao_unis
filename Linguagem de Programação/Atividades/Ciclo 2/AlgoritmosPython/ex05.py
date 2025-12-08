"""
Escreva uma função que:
Receba uma frase como parâmetro.
Retorne uma nova frase com cada palavra com as letras invertidas.

"""


def inverter_palavras(frase):
    palavras = frase.split()
    invertidas = [p[::-1] for p in palavras]
    nova_frase = " ".join(invertidas)
    return nova_frase

frase = input("Digite uma frase: ")
print(inverter_palavras(frase))
