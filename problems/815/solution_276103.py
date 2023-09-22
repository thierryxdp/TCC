def insere(lista_numero,n):
    '''Dada uma lista de inteiros crescentes e um número
    n, inclui o número na posição correta da lista.
    assinatura: list, int -> list '''
    lista = lista_numero + [n,]
    list.sort(lista)
    return lista