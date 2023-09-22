def filtraMultiplos(lista,n):
    '''retorna uma nova lista com todos os elementos da lista original que
    forem divisíveis por n;
    list, float -> list'''
    
    elemento = 0
    novalista = []
    
    while elemento < len(lista):
        if lista[elemento] % n == 0:
            list.append(novalista,lista[elemento])
        elemento = elemento + 1
        
    return novalista