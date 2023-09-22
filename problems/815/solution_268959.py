def insere(lista_numero,n):
    """Ao inserir uma lista e um determinado número 'n'
    retorna esse numero 'n' na posição respectiva ao seu valor."""
    list.sort(lista_numero)
    lista_numero.insert(n,n)
    return lista_numero