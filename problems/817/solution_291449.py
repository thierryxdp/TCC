def acima_da_media(lista):
    list.sort(lista)
    a=sum(lista)
    b=len(lista)
    med=a/b
    c=list.index(lista, med)
    del lista[0:c] 
    return lista