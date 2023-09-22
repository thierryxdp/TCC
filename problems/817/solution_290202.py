import math
def acima_da_media(notas):
    '''com'''
    media=sum(notas)/len(notas)
    funcao= [notas]+[media]
    list.sort(notas)
    media=math.ceil(media)
    return media