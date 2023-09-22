def insere(lista_numero, n):
    """Função que dada uma lista ordenada crescente de números inteiros(lista_numero)
    e um número inteiro(n), e retorna a lista dada com a inclusão de (n) na posição em
    que a lista continue ordenada; list, int -> list """

    list.append(lista_numero,n)
    list.sort(lista_numero)

    return lista_numero