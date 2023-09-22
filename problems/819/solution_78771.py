def filtraMultiplos(lista,num):
    '''Recebe uma lista de números e um número num e retorna 
       uma lista com os múltiplos de num dentro da lista;
       list, int -> list'''
    
    multiplos = []
    
    for n in lista:
        
        if n % num == 0:
            
            multiplos.append(n)
            
    return multiplos