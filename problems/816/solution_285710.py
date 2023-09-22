def maiores(lista, n):
    
    for dado in lista:
        
        if n > dado:
            
            lista.remove(dado)
            
    return lista