def insere(lista_numero, n):
    """Recebe uma lista ordenada de números e um número qualquer, e retorna o
    a lista com o número inserido na sequência ordenada"""
    lista_numero = lista_numero + [n]
    list.sort(lista_numero)
    return lista_numero