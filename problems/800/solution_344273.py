def total(lista,produtos):
    '''função que recebe uma lista de compras e um dicionario
     contendo o preço de cada produto disponivel em uma
     determinada loja, e retorna o valor total dos itens da 
     lista que estejam disponiveis nesta loja;
     list, dic -> float'''
    s = 0
    for i in lista:
        if i in list(dict.keys(produtos)):
            s += produtos[i]
        else: 
            s = s
    return round(s,2)