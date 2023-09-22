def filtraMultiplos(lista_numeros, n):
    
    lista_multiplos = []
    i = 0
    while i <= lista_numeros:
        if lista_numeros % n == 0:
            list.append(lista_numeros[i] ,lista_multiplos)
        i +=1