def total(lista,dicionario):
    '''Recebe uma lista de compras e um dicionario com o preço 
    de cada produto em uma loja e retorna o preço total da compra
    a ser feita; list, dicionario -> float'''
    precos = []
    for produtos in lista:
        if produtos in dict.keys(dicionario):
            precos += [dicionario[produtos]]
    return round(sum(precos),2)