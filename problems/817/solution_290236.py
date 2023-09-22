import math
def acima_da_media(notas):
    '''com'''
    media=sum(notas)/len(notas)
    list.sort(notas)
    funcao= [notas]+[media]
    funcao2= notas[:]+[media]
    list.sort(funcao2)
    ident=list.index(funcao2,media)
    return funcao2[ident:]