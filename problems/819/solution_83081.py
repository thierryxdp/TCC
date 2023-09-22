def filtraMultiplos(lista_nums,n):
    '''Retorna uma lista contendo apenas os múltiplos de n;
    [int]->[int]'''
    
    i=0
    lista=[]
    
    while i<len(lista_nums):
        if lista_nums[i]/n==0:
            lista.append(lista_nums[i])
        i+=1
    return lista