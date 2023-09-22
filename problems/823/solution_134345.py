def faltante(lista):
    """funcao que dada uma lista com n-1 inteiros, retorna qual numero inteiro do intervalo fornecido como lista esta faltando
    list(int)--->int"""
    list.sort(lista)
    lista=lista
    i=0
    faltante=0
    if 1 not in lista:
        return 1
    while i+1<len(lista):
        if lista[i]+1!=lista[i+1]:
            faltante=faltante+lista[i]+1
            return faltante
        i=i+1
        else:
            return lista[-1]+1