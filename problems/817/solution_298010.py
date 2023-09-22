def maiores(lista:list,n:int)->list:
    lista.append(n)#adiciona "n" na lista
    lista.sort() #reorganiza a lista em ordem crescente
    lista=lista[(lista.index(n)+1):]#Recorta a lista no intervalo após n 
    
    return lista

def acima_da_media(lista):
    
    
    x=lista.pop()
    lista.append(x)
    media=sum(lista)/(lista.index(x))
    lista=maiores(lista,(media))
    lista.remove(media)
    return lista