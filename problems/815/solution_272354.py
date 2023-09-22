def insere(lista_numero,n):
    '''
    	Funcao recebe uma lista ordenada de numeros
        inteiros e um numeros inteiro n e retorna
        a lista dada incluindo n ordenada
        list -> list
        
    '''
    return list.sort(list.extend(lista_numero,[n,]))