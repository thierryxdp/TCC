def acima_da_media(lista:list)->list:
    
    x=lista.pop()#tira o ultimo elemento da lista e salva em uma variavel
    lista.append(x)#retorna x a lista
    media=sum(lista)/(lista.index(x)+1)#faz a media
    lista=maiores(lista,media)#aplica função maiores
    lista.sort()#organiza lista	
    return lista

def maiores(lista:list,n:int)->list:
    lista.append(n)#adiciona "n" na lista
    lista.sort()#organiza a lista
    #reversed(lista) #reorganiza a lista em ordem crescente
    lista=lista[-1:lista.index(n):-1]#Recorta a lista no intervalo invertido 
    if n in lista: #testa se a média esta na lista
        lista.remove(n)#remove a média da lista
    	return lista
    else:
    	return lista