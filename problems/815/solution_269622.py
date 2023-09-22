def insere(lista_numero, n):
    '''dada uma lista com números inteiros em ordem crescente e um número inteiro n
    qualquer, inclui n na lista de forma que ela continua ordenada e crescente;
    lista, int --> lista'''
    lista_com_n = lista_numero + [n,]
    list.sort(lista_com_n)
    return lista_com_n