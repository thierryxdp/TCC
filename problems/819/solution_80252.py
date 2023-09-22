def filtraMultiplos(lista, n):
    ''' Função que filtra os múltiplos de um dado
        número contidos em uma dada lista. 
        list, int -> list '''
    
    lista_final = []
    i = 0
    
    while i < len(lista):
        
        if lista[i]%n == 0:
            lista_final.insert(i, lista[i])
        
        i = i + 1
        
    return lista_final