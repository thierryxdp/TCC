def faltante(lista):
    '''dada uma lista com N − 1 inteiros numerados de 1 a N,
 descobre qual número inteiro deste intervalo está faltando'''
    lista=sorted(lista)
    indice=1
    while indice<len(lista):
        if lista[indice]!=lista[indice-1]+1:
            return lista[indice]-1
        indice+=1
    return 'what'