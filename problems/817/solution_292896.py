import math
def acima_da_media(lista):
    media=sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    posicao=list.index(lista,media)
    
    
    return lista[posicao+1:]