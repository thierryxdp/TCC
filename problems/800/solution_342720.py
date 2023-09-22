def total(lista,dicionario):
    '''funçao que receve uma lista de compras e um dicionario contendo
o preço de cada produto disponivel em uma determinada loja, e retornar
o valor total dos itens da lista.
list,dict -> float'''
    valor=[]
    for c in lista:
        valor.append(dicionario[c])
    return round(sum(valor),2)