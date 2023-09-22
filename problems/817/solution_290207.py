import math
def acima_da_media(notas):
    '''com'''
    media=sum(notas)/len(notas)
    funcao= [notas]+[media]
    list.sort(notas)
    list.index(funcao,media)
    return x