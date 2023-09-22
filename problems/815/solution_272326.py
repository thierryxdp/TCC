def insere(lista_numero,n):
    '''insere um certo numero n em uma lista de numeros ordenada de maneira crescente 
    de modo que a lista continue ordenada de maneira crescente;
    list,int->list'''
    l=lista_numero
    l=list.append(l,n)
    l=list.sort(l)
    return l