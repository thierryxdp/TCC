def insere(lista_numero,n):
    '''
    Função que recebe uma lista de numeros e um numero n 
    e retorna uma nova lista que inclui n na posição de modo 
    que essa nova lista continue ordenada
    list, int -> list
    '''
    
    lista_numero.append(n)
    lista_numero.sort()
    
    return lista_numero