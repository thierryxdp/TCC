def total (lista, mercado):
    '''Dado uma lista e um dicionário conrendo preços de cada produto,
retorna o valor total dos itens da lista que estejam disponíveis na loja.lista,dicionário-->float''' 
    valor = 0
    for i in lista:
        if i in mercado:
            valor = valor + mercado[i]
    return round(valor,2)