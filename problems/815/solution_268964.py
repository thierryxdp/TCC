def insere(lista_numero,n):
    """Ao inserir uma lista e um determinado número 'n'
    retorna esse numero 'n' na posição respectiva ao seu valor."""
    lista_numero.insert(n,n)
    lista_numero.sort()
    return lista_numero