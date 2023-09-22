def conta_numero(n,m:
    '''Essa função que dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz'''
    '''int,list->int'''
     qt=0
    for numeros in m:
        for i in numeros:
            if i == n:
                qt+=1
    return qt