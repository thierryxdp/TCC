def faltante(lista):
    """dada uma lista com N-1 inteiros numerados de 1 a N,retorna o número que falta.
    list->int"""
    L=list.sort(lista)
    i=0
    while L(i+1)-L(i)==1:
        i=i+1
    return L(i)