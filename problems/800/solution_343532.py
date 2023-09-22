def total(lista=[], disponiveis={}):
    '''
    funcao que recebe uma lista compras e um dicionario 
    com os produtos do mercado e seus preços e retorna 
    os produtos disponiveis com o preço
    list,dict->float
    '''
    x = 0.0
    for i in lista:
        x += disponiveis[i]
    return round(x,2)