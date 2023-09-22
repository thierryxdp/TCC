def intercala(lista1, lista2):
    '''
        Função gera uma lista L3 que é formada intercalando os elementos de L1 e L2.
        Str => Str
    '''
    n = len(lista1)
    lista3 = []
    
    for i in range(n):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
    
    return lista3