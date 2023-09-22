def filtraMultiplos(lista_numeros,n):
    '''
    list, int ---- > list
    funcao recebe uma lista de numeros, um numero inteiro
    e retorna em uma lista os numeros da lista recebida que 
    sao divisiveis pelo numero da entrada
    '''
    lista_final = []
    i = 0
    while i < len(lista_numeros):
        if lista_numeros[i]%n==0:
            lista_final += [lista_numeros[i]]
        i+=1
    return lista_final