def total(produto,dicionario):
    '''fucao que calcula os valores de produtos escolhidos em um dicionario
    list,dict->float'''
    soma=0
    comprar=0
    for comprar in range(0,len(produto)):
        if produto[comprar] in dicionario.keys():
            soma=dicionario[produto[comprar]]+soma
    return round(soma,2)