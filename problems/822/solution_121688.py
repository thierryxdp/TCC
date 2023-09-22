def repetidos(listaNumeros):
    ''' Recebendo como entrada uma lista de numeros, a funcao diz o numero de
    vezes que o elemento da lista eh igual ao elemento anterior;
    
    list -> int '''
    
    list.append(listaNumeros,'')
    indice_lista1 = 0
    indice_lista2 = 1
    elemento1 = listaNumeros[0]
    elemento2 = listaNumeros[1]
    vezes = 0
    
    while indice_lista2 + 1 < len(listaNumeros):
        
        if elemento1 == elemento2: 
            
            vezes = vezes + 1
            
        indice_lista1 = indice_lista1 + 1
        indice_lista2 = indice_lista2 + 1
        elemento1 = listaNumeros[indice_lista1]
        elemento2 = listaNumeros[indice_lista2]
        
    return vezes