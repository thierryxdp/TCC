def filtra_pares(numeros):
    '''
    funcao que recebe uma tupla com 4 numeros e verifica 
    quais sao pares e os retorna
    param:
    numeros - tupla(inteiros)
    retorna - tupla
    '''
    num_pares = ()
    
    if num[0]%2 == 0:
        num_pares = num_pares + (numeros[0],)
        
    if num[1]%2 == 0:
        num_pares = num_pares + (numeros[1],)
        
    if num[2]%2 == 0:
        num_pares = num_pares + (numeros[2],)
        
    if num[3]%2 == 0:
        num_pares = num_pares + (numeros[3],)
        
    return num_pares