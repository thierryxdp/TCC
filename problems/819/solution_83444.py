def filtraMultiplos(ista_numeros, n):
    
    lista_multiplos = []
    i = 0
    while i <= (len(lista_numeros)-1):
        if lista_numeros[i] % n == 0:
			lista_multiplos[0:0] = [lista_numeros[i]]
        i +=1 
        
    return lista_multiplos