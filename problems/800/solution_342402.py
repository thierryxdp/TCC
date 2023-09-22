def total(lista, dicionario):
    "função que retorna o preço total da lista de compras dado um dicionário"
    "list, dicionario -> float"
    soma=0
    for item in lista:
        if item in dicionario:
            soma +=dicionario[item]
    return round(soma,2)