import math
def acima_da_media(lista):
    media=math.ceil(sum(lista)/len(lista))
    list.append(lista,media)
    list.sort(lista)
    posicao=list.index(lista,media)
   
    if media in lista:
        return lista[posicao+2:]
    else:
    	return lista[posicao+1:]