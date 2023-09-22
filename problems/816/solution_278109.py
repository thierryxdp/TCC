def maiores(lista_inteiros, n):
    
    lista_inteiros.sort()
    
    if n in lista_inteiros == True:
        cont = lista_inteiros.index(n)
        
        lista_maiores = lista[cont:-1]
        
        return lista_maiores