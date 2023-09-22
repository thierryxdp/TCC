def total(lista, preco):
"""funcao recebe string lista e retorn dicionario contendo o preco de cada produto""" 
    soma = 0
    for x in lista:
        soma = soma + preco[x]
    return round(soma, 2)