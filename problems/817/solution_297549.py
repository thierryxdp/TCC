def acima_da_media(lista):
    lista=maiores(lista,6.9)
    return lista

def maiores(lista:list,n:int)->list:
    lista.append(n)#adiciona "n" na lista
    lista.sort() #reorganiza a lista em ordem crescente
    lista=lista[(lista.index(n)+1):]#Recorta a lista no intervalo após n 
    return lista