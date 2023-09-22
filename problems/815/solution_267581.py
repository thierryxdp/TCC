def insere(lista_numero,n):
    ''' Dando como entrada uma lista ordenada crescente e um numero n, a 
    funcao retorna uma nova lista, mas agora com o novo numero n e ainda
    em ordem crescente, de forma que o n se encaixe corretamente na se-
    quencia; 
    
    list, int (ou float) -> list '''
    
    list.append(lista_numero,n)
    list.sort(lista_numero)
    
    return lista_numero