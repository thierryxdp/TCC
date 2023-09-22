def insere(lista_numero,n):
    '''Esta função inclui n na sequência crescente de números inteiros dada.
    list, int -> list'''
    lista = list.append(lista_numero,n)
    lista = list.sort(lista)
    return lista