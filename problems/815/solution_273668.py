def insere(lista_numero,n):
    """A função retorna uma lista ordenada(crescente) e coloca um n
    na ordem certa dentro lista
    list--int-->list"""
    nova_lista = lista_numero + [n]
    return list.sort(nova_lista)