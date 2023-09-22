def total(lista=[],dict={}):
    '''Recebe uma lista de compras e um dicionario
    contando o preço de cada produto disponivel e 
    retorna o valor total dos itens disponiveis'''
    cont=0.0
    for i in lista:
        cont+=dict[i]
    return round(cont,2)