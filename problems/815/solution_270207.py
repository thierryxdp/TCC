def insere(lista_numero, n):
    """ dada uma lista de números inteiros em ordem 
    crescente e um numero inteiro n, retorna a lista com o n
    adicionado, de forma com que a lista continue crescente;
    list, int -> list"""
    a = list.append(lista_numero, n)
    return list.sort(a)