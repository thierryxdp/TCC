def insere(lista_numero,n):
    '''Função que inclui um inteiro qualquer(n) em uma lista
    que contem vários outros inteiros e gerando uma nova
    lista de forma ordenada contendo esse novo inteiro(n).
    list, int -> list'''
    lista1=lista_numero.append(n)
    lista2=list.sort(lista_numero)
    return lista_numero