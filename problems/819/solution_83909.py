def filtraMultiplos(numeros, n):
    '''Função que retorna uma nova lista contendo os elementos da listaa original (números)
    que são divisíveis por número n.
    list[int], int => list[int]'''
    i=0
    filtrados=[]
    while i<len(numeros):
        if numeros[i]%n==0:
            filtrados.append(numeros[i])
        i+=1
    return filtrados