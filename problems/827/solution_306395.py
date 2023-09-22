def qtd_divisores(n):
    '''---'''
    
    numero = n
    lista = ''
    
    for indice in range(1, n+1):
        if numeros % indice == 0:
            lista.append(indice)
    return len(lista)