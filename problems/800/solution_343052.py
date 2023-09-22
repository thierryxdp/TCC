def total(lista, dicio):
    ''' função que recebe uma lista de itens e um dicionario contendo o preço de cada produto e retorna o valor total do itens'''
    item1,item2,item3 =lista
    return dicio[item1] +dicio[item2]+dicio[item3]