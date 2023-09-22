def total(lista_compras,preço):
    '''
        funcao que recebe uma lista de compras e um dicionario
        contendo o preco de cada produto disponıvel em uma
        determinada loja, e retorna o valor total dos itens da lista que
        estejam dispon ́ıveis nesta loja.
        lista:list
        lista_compras:list
        preço:dict
        return:float
    '''
    
    lista = []
    for i in range(len(lista_compras)):
        if lista_compras[i] in preço:
            lista.append(preço[lista_compras[i]])
    return sum(lista)