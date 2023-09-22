def faltante(lista):
    """dada uma lista com n-1 inteiros numerados de 1 a n, retorna o numero inteiro que ta faltando
    list->int"""
    f=1
    proximo=0
    while f<len(lista)+1:
        if f!= lista[proximo]:
            return f
        proximo= proximo+1
        f=f+1