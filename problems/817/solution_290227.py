import math
def acima_da_media(notas):
    '''com'''
    media=sum(notas)/len(notas)
    list.sort(notas)
    funcao= [notas]+[media]
    ident=list.index(funcao,media)
    funcao2= notas[:]+[media]
    list.reverse(funcao2)
    return funcao2