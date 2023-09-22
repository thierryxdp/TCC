def insere(lista_numero,n):
    '''insere um certo numero n em uma lista de numeros ordenada de maneira crescente 
    de modo que a lista continue ordenada de maneira crescente;
    list,int->list'''
    l1=list.append(lista_numero,n)
    l1=list.sort(l1)
    return l1