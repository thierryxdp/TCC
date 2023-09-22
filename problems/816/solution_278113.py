def maiores(lista_inteiros, n):
    
    lista_maiores.append(n)
    lista_inteiros.sort()
    
    cont = lista_inteiros.index(n)
        
    lista_maiores = lista[cont:-1]
        
    return lista_maiores