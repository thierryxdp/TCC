def filtraMultiplos(lista,n):
    '''Função filtra os múltiplos de N e anexa numa nova lista de múltiplos;
    list, int ->list'''
    i=0
    lista2 = []
    
    while  i<len(lista):
        if lista[i] % n == 0:
            lista2.append(lista[i])
        i+=1        
    return lista2