def filtraMultiplos(lista_numeros, n):
    
    lista_multiplos = []
    i = 0
    while i <= (len(lista_numeros)-1):
        if lista_numeros[i] % n == 0:
			lista_multiplos[0:0] = [lista_numeros[i]]
        i +=1 
        
        
    list.sort(lista_multiplos)    
    return lista_multiplos