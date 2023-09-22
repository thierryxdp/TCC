def insere(lista_numero, n):
    """ list, int -> list;
    Função que recebe uma lista de números inteiros de modo
    ordenado(crescente) e retorna a mesma lista com o
    número n adicionado a ela, na possição correta, é claro,
    para que a lista continue ordenada."""
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero