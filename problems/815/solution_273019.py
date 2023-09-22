def insere(listaNumeroOrdenada,n):
    """dado uma lista e um numero inteiro retorna uma outra lista com o numero inserido de acordo com a posicao ordenada
    list[int],n:int -> list[int]"""
    ListaNumeroOrdenada.append(n)
    ListaNumeroOrdenada.sort()
    return ListaNumeroOrdenada