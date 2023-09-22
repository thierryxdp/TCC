def insere(lista_numero,n):
    '''
    Funçao que recebe uma lista de numeros e um numero e retorna a lista
    com o numero inserido na ordem crescente
    list, float -> list
    '''
    list.insert(lista_numero,0,n)
    list.sort(lista_numero)
    return lista_numero