def insere(list_numero,n):
    '''Função que dado uma lista(list_numero) e um número(n), o número é 
    inserido na lista em sua posição correta assim não alterando a ordem da lista
    list->list , int->list'''
    L= list_numero
    list.insert(L,2,n)
    L.sort()
    return L