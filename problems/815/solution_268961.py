def insere(lista_numero,n):
    """Ao inserir uma lista e um determinado número 'n'
    retorna esse numero 'n' na posição respectiva ao seu valor."""
    list.sort(lista_numero)
    indice = lista_numero.index(n) 
    lista_numero[indice:indice] = [n]
    return lista_numero