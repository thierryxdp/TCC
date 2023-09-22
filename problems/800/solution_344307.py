def total(lista, dicionario):
    '''retorna o valor total da soma de precos de todas as compras da lista'''
    soma=0
    for i in lista:
        soma+=dict.get(dicionario, i)
    return round(soma, 2)