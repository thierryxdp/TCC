def total(lista, preco):
"""FUNCAO RECEBE UMA STRING/LISTA E UM DICIONARIO CONTENDO O PRECO DE CADA PRODUTO"""
    soma = 0
    for x in lista:
        soma = soma + precos[x]
    return round(soma, 2)