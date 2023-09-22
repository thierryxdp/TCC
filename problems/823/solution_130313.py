def faltante(numeros):
    '''essa função recebe uma lista de numeros e 1 até N, e retorna oq está entre elas'''
    i = int()
    if 1 not in numeros:
        numeros.insert(0,1)
    while i<len(numeros):
        if numeros[i]+1 not in numeros:
            numeros.insert(i,numeros[i]+1)
        i +=1 
    numeros.sort()
        
    return numeros