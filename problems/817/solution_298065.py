def acima_da_media(lista):
    int(media)=sum(lista)/(lista.index(x)+1)
    x=lista.pop()
    lista.append(x)
   
    lista=maiores(lista,media)
    lista.remove(media)
    return lista

def maiores(lista:list,n:int)->list:
    lista.append(n)#adiciona "n" na lista
    lista.sort() #reorganiza a lista em ordem crescente
    lista=lista[(lista.index(n)):]#Recorta a lista no intervalo após n 
    return lista