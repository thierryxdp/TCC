def filtraMultiplos(lista,n):
    '''---'''
    
    numero_elementos = len(lista)
    indice = 0
    lista_final = list()
    
    while indice < numero_elementos:
        if lista[indice] // n == n:
            list.append(resposta, lista[indice])
       
    	indice += 1
        
    return tuple(lista_final)