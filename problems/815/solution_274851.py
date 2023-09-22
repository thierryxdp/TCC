def insere(lista_numero, n):
    """Recebe uma lista e um número inteiro, acrescentando esse número inteiro à lista e a ordenando de forma crescente.
    testes: insere([1,2,3], 4) == [1,2,3,4]
    insere([3,2,1], 4) == [1,2,3,4]
    assinatura: list, int --> list
    """
    ls = lista_numero
    ls.append(n)
    list.sort(ls)
    return ls