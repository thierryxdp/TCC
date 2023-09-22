def filtraMultiplos (lista, n):
    '''
    	essa função recebe uma lista de números e extrai somente os números dela 
        divisiveis por n
        list,int-> lits
    '''
    x = []
    i = 0
    while i< len(lista):
        if lista[i]% n == 0:
            x.append(lista[i])
            i = i+1
    return x