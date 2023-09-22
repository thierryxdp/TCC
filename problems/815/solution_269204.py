def insere(lista_numero,n):
    """ esta função irá incluir o numero inteiro "n" na posição correta na lista_numero
    entrada -> lista, int
    saida -> lista """
    list.append(lista_numero, n)
    list.sort(lista_numero)
    return lista_numero