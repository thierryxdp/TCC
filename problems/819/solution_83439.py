def filtraMultiplos(lista_numeros, n):
    
    lista_multiplos = []
    i = 0
    while i <= len(lista_numeros):
        if lista_numeros[i] % n == 0:
            list.append(lista_multiplos ,lista_numeros[i])
        i +=1 
        
    return lista_multiplos