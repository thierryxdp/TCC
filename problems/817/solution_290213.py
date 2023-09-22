import math
def acima_da_media(notas):
    '''com'''
    media=sum(notas)/len(notas)
    funcao= [notas]+[media]
    list.sort(notas)
    ident=list.index(funcao,media)
    funcao2= notas[:]+[media]
    return funcao2