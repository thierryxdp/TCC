def maiores(lista:list,n:int)->list:
    lista.append(n)#adiciona "n" na lista
    lista.sort() #reorganiza a lista em ordem crescente
    lista=lista[(lista.index(n)):]#Recorta a lista no intervalo após n 
    lista.remove(n)
    return lista