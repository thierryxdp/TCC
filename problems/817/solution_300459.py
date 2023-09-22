def maiores(lista,n):
    list.append(lista,n)
    list.sort(lista)
    a=list.index(lista,n)
    return lista[a+1:]
media=sum(lista)/len(lista)
if(media in lista):
    c=maiores(lista,media)
    return c[1:]
else:
    return maiores(lista,media)