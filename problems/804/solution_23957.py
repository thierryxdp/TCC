def filtra_pares(numeros=(0,0,0,0)):
    lista_numeros = list(numeros)
    numero1 = lista_numeros.pop(0)
    numero2 = lista_numeros.pop(0)
    numero3 = lista_numeros.pop(0)
    numero4 = lista_numeros.pop(0)
    
    if numero1 % 2 == 0:
        lista_numeros.append(numero1)
    if numero2 % 2 == 0:
        lista_numeros.append(numero2)
    if numero3 % 2 == 0:
        lista_numeros.append(numero3)
    if numero4 % 2 == 0:
        lista_numeros.append(numero4)
        
    numeros = tuple(lista_numeros)
    return numeros