def insere(lista_numero, n):
    """Dada uma lista ordenada de números inteiros e um número
    inteiro n, inclua n na posição correta, ou seja, de tal maneira
    que a lista continue ordenada
    Assinatura: list, int -> list
    """
    lista_numero.append(n)
    listaO1=sorted(lista_numero)

    return listaOrganizada