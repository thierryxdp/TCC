def maiores(lista,n):
    '''funcao que dada uma lista de numeros int e um numero n int, retorna outra lista com todos os numeros maiores que n de forma crescente'''
    '''int,int=>int'''
    maiores=list()
    lista.sort()
    for c in lista:
        if c >= n:
            maiores.append(c)
    return maiores


def acima_da_media(nota):
    soma=sum(nota)
    Ni=len(nota)
    media=(soma//Ni)
    list.append(nota,media)
    list(nota)
    i=list.index(nota,media)
    return media