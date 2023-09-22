def insere(lista_numero,n):
    '''insere um certo numero n em uma lista de numeros ordenada de maneira crescente 
    de modo que a lista continue ordenada de maneira crescente;
    list,int->list'''
    lista=list.append(lista_numero,n)
    lista=list.sort(lista_numero)
    return lista