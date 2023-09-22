def insere(lista_numero,n):
    """dada uma lista ordenda(crescente) de números inteiros e um número inteiro n, a função retorna
    o número n na posição correta, de tal maneira que a lista continue ordenada;
    list,int->list"""
    A=lista_numero
    list.append(A,n)
    list.sort(A)
    return A