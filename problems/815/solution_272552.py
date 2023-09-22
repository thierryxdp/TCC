def insere(lista_numero,n):
    """ Dada um lista ordenada de numeros inteiros e um número inteiro n, insere n em uma posição onde a lista permanece ordenadada.
    list,int->int"""
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero