def insere(lista_numero,n):
    """Funcao que, dados uma lista ordenada e um numero inteiro n, retorna
    uma nova lista ordenada com n inserido;
    Entrada: list, int
    Saida: list"""

    lista = lista_numero + [n]
    list.sort(lista)
    return lista