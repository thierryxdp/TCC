def filtraMultiplos(lista,n):
    '''---'''
    
    numero_elementos = len(lista)
    indice = 0
    lista_final = list()
    
    while indice < numero_elementos:
        if lista[indice] // n == n:
            list.append(lista_final, lista[indice])
       
    	indice += 1
        
    return lista_final