import math as m

def  acima_da_media(l):
    ''' Retorna uma losta com as notas de l que ficaram acima da média
    list -> list'''
    g=[]
    for x in l:
        if x>(m.fsum(l)/len(l)):
            g.append(x)
        
            
    list.sort(g,reverse=False)
    
    return g