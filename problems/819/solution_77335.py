#---------------------EXERCICIO 1---------------------

def filtraMultiplos (lista_numeros, numeroN):
    '''Retorna numeros divisiveis por numeroN
       list, float -> list'''
    
    i = 0     			#contador
    lista_nova = []     #acumulador
    
    while i<len(lista_numeros):
        if lista_numeros[i] % numeroN == 0:
            list.append(lista_nova, lista_numeros[i])
        i += 1
    
    return lista_nova