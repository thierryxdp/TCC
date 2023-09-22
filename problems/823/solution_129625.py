def faltante(lista):
    '''retorna qual número inteiro está faltando na lista;
    list -> int'''
    
    n = len(lista)
    lista_real = list(range(1,n+2,1))
    posicao = 0
    faltou = 0
    
    while posicao < n+1:
        if lista_real[posicao] not in lista:
            faltou +=lista_real[posicao]
        posicao += 1
    
    return faltou