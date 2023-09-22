def total(lista, preco):
    soma = 0
"""funcao recebe string lista e retorn dicionario contendo o preco de cada produto""" 
    for x in lista:
        soma = soma + preco[x]
    return round(soma, 2)