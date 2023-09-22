def maiores(lista,n):
    list.append(lista,n)
    list.sort(lista)
    a=list.index(lista,n)
    lista[a+1:]
	media=sum(lista)/len(lista)
  	return maiores(lista,media)