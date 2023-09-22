def filtraMultiplos(lista,n):
    '''---'''
    
    numero_elementos = len(lista)
    indice = 0
    lista_final = list()
    
    while indice < numero_elementos:
        if lista[indice] % n == 0:
            list.append(lista_final, lista[indice])
       
    	indice += 1
        
    return list(lista_final)