import math
def acima_da_media(notas):
    '''com'''
    lista=[notas]+[media]
    media=sum(notas)/len(notas)
    funcao= [notas]+[media]
    list.sort(notas)
    ident=list.index(funcao,media)
    return funcao