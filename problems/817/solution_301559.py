def maiores(lista,n):
    lista.append(n)
    lista.sort()
    i=lista.index(n)
    return lista[i+1:]

def acima_da_media(lista):
    med=sum(lista)/len(lista)
    acima>med
    lista=maiores(lista,acima)
    return lista