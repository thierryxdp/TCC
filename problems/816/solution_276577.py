def maiores(lis,n):
    '''procura os numeros maiores que n em uma lista e retorna uma lista com eles
    list,int->list'''
    maiores_numeros=list()
    for c in lis:
        if c>=n:
            maiores_numeros.append(c)
    return sorted(maiores_numeros)