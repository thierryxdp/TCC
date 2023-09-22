def maiores(lista_inteiros, n):
    
    lista_inteiros.append(n)
    lista_inteiros.sort()
    
    cont = lista_inteiros.index(n)
        
    listamaiores = lista[cont:-1]
        
    return lista_maiores