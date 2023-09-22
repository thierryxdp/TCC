def total(lista,d):
    '''
    funcao retorna o valor total das comprasda lista de entrada
    '''
    soma=0
    for i in lista:
        soma=soma+d[i]
    return round(soma,2)