def insere(lista_numero,n):
    """Dada uma função com uma lista e um número inteiro, a função irá inserir
    o inteiro dentro da lista, e irá ordenar por ordem numérica crescente.
    list -> int -> list"""
    lista_nova = lista_numero + [n]
    list.sort(lista_nova)
    return lista_nova