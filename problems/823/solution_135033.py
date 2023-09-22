def faltante(lista):
    '''dada uma lista com numeros inteiros, em geral, ordenados, retorna o inteiro que está faltando
    list-->int'''
    i=0
    N=len(lista)+1
    list.sort(lista)
    if lista[0]!=1:
        return 1
    if lista[-1]<N:
        return N
    while i+1<len(lista):
        if lista[i+1]!=lista[i]+1:
            return lista[i]+1
        i=i+1