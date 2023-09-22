def faltante(lista):
    '''Função que dada uma lista com (n-1) inteiros numerados de 1 a n, descobre qual número inteiro desse intervalo está faltando
    lista -> int'''
    list.sort(lista)
    if 1 not in lista:
        return 1
    elif len(lista)==lista[-1]:
        return len(lista)+1
    else:
        i=0
        while lista[i]+1==lista[i+1]:
            i=i+1
        return i+2