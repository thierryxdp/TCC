def insere(lista_numero,n):
    """Inclui o numero n na lista ordenada (crescente) na posicao
    correta de maneira que a lista continue ordenada;
    list,int->list"""
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero