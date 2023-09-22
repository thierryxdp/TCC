def maiores(lista,n):
    list.append(lista,n)
    list.sort(lista)
    g=list.index(lista,n)
    return lista[g+1:]
media= sum(lista)/len(lista)
d=maiores(lista,media)
if (media in lista):
    return d[1: ]
else:
    return maiores(lista,media)