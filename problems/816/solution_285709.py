def maiores(lista, n):
    
    for dado in lista:
        
        if dado<n:
            
            lista.remove(dado)
            
    return lista