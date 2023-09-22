def maiores(lista, n):
    
    lista.sort()
    
    for dado in lista:
        
        if n > dado:
            
            lista.remove(dado)
            
    return lista