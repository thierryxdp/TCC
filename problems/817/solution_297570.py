def acima_da_media(lista):
    
    
    x=lista.pop()
    lista.append(x)
    media=sum(lista)/(lista.index(x)+1)
    lista=maiores(lista,int(media))
    return lista

def maiores(lista:list,n:int)->list:
    lista.append(n)#adiciona "n" na lista
    if (lista[n]>sum(lista)):
    lista.sort() #reorganiza a lista em ordem crescente
    
    	lista=lista[(lista.index(n)+1):]#Recorta a lista no intervalo após n 
    	return lista
    else:
        return []