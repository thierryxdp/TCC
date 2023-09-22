def faltante(lista):
    """funcao que dada uma lista com n-1 inteiros, retorna qual numero inteiro do intervalo fornecido como lista esta faltando
    list(int)--->int"""
    i=0
    n=lista[-1]
    lista=list.sort(lista)
    while i<len(lista):
        if lista[i]==lista[i+1]+1:
            i=i+1
        else:
            return lista[i+1]+1