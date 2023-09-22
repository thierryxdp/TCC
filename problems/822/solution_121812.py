def repetidos(numeros):
    '''retorna o numero de vezes que um elemento é igual ao anterior
    list->int'''
    i=1
    con=0
    while i<=len(numeros)-1:
        if numeros[i]==numeros[i-1]:
            con+=1
        i+=1
    return con