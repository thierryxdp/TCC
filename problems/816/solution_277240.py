def maiores(lista_nume_inteiros,n):
    '''Função que dado uma lista(lista_nume_inteiros) e um número(n), retorna uma outra
    lista com todos os numeros maiores que n existentes na lista dada.
    list->list, int->list'''
    L=lista_nume_inteiros
    list.insert(L,2,n)
    L.sort()
    k=list.index(L, n)
    return L[k+1: ]