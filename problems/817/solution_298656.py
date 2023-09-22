def acima_da_media(lista):
    
    x=lista.pop()
    lista.append(x)
    media=sum(lista)/(lista.index(x)+1)
    lista=maiores(lista,media)
    lista.sort()	
    return lista

def maiores(lista:list,n:int)->list:
    lista.append(n)#adiciona "n" na lista
    lista.sort()
    #reversed(lista) #reorganiza a lista em ordem crescente
    lista=lista[-1:lista.index(n):-1]#Recorta a lista no intervalo após n 
    if n in lista:
        lista.remove(n)
    	return lista
    else:
    	return lista