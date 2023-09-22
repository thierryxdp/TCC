def filtraMultiplos(lista,n):
    
    nova_lista = []
    
    indice = 0
    
    while (indice < len(lista)):
        
        if (lista[indice] % n == 0):
            
            list.append(nova_lista,lista[indice])
            
            indice = indice + 1
            
    return    nova_lista