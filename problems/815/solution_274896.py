def insere(lista_numero, n):
    '''Recebe uma lista crescente de numeros 
    inteiros (lista_numero) e umnúmero inteiro (n),
    retornará a lista com n na posição correta
    
    list, int -> list
    '''
    
    lista_numero.insert(0, n)
    list.sort(lista_numero)
    return lista_numero