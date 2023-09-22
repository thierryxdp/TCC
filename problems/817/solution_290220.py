import math
def acima_da_media(notas):
    '''com'''
    media=sum(notas)/len(notas)
    funcao= [notas]+[media]
    ident=list.index(funcao2,media)
    funcao2= notas[:]+[media]
    list.sort(funcao2)
    return funcao2[ident:]