def total(lista,dicio):
    '''função que recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível em uma determinada loja, e retorna o valor total dos itens da lista que estejam disponíveis nesta loja.
      list->dicionário'''
    soma=0
    indece=0
    while indece<len(lista):
        if lista[indece] in dicio:
            soma=soma+dict.get(dicio,lista[indece])
        indece=indece+1
    return round(soma,2)