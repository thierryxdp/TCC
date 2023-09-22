def acima_da_media(lista:list)->list:
    lista=maiores(lista,(media)) #chamada da função
    return lista

def maiores(lista:list,n:int)->list:
    lista.append(n)#adiciona "n" na lista
    lista.sort() #reorganiza a lista em ordem crescente
    lista=lista[(lista.index(n)):]#Recorta a lista no intervalo após n 
    lista.remove(n)
    return lista