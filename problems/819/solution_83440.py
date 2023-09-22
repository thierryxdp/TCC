def filtraMultiplos(lista_numeros, n):
    
    lista_multiplos = []
    i = 0
    while i <= (len(lista_numeros)-1):
        if lista_numeros[i] % n == 0:
            list.append(lista_numeros[i] ,lista_multiplos)
        i +=1 
        
    return lista_multiplos