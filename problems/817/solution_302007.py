import math as m

def  acima_da_media(l):
    ''' Retorna uma losta com as notas de l que ficaram acima da média
    list -> list'''
    for x in l:
        if x<= m.media(l):
            l.remove(x)
    list.sort(l,reverse=False)
    
    return l