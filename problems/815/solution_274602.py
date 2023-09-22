def insere(lista_numero,n):
    '''Recebe uma lista e um número inteiro, inclue o numero
    na posição correta
    list, int->list
    '''
    lista2= lista_numero + [n]
    list.sort(lista2)
   
    return lista2