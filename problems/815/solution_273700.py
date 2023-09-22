def insere(lista_numero,n):
    '''retorna uma lista com os numeros da lista lista_numero e o numero inteiro n
    em ordem crescente
    list,int->list'''
    return list.sort(lista_numero+[n])