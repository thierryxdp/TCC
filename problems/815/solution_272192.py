def insere(lista_numero,n):
    """funcao que dada uma lista de números e um número inteiro n, insere n na lista, que por sua vez possui seus elementos em ordem crescente;
    list de int -> list de int"""
    nova_lista_numero=list.sort(list.append(lista_numero,n))
    return niva_lista_numero