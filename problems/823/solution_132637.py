def faltante(lista):
    ''' função que dada uma lista com n numeros inteiros numerados de 1 a
    n, faltando um numero, descubra qual está faltando; int-->int'''
    list.sort(lista)
    n=lista[-1]
    lista_compara=list(range(1,n+1))
    proximo=0
    while lista[proximo]==lista_compara[proximo]:
        proximo=proximo+1
    return lista_compara[proximo]