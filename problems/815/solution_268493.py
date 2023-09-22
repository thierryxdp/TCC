def insere(lista_numero, n):
    '''dada uma lista ordenada crescente e um numero n, insere o número n na posição correta para
    que a lista continue crescente.
    lista + int -> lista'''
    lista = list.append(lista_numero, n)
    bonito = list.sort(lista)
    return bonito