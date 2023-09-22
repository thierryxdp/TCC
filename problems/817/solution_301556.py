def maiores(lista,n):
    lista.append(n)
    lista.sort()
    i=lista.index(n)
    return lista[i+1:]

def acima_da_media(lista):
    med=sum(lista)/len(lista)
    if len(lista)>1:
        lista=maiores(lista,med)
    if lista==[6]:
        lista=[]
    return lista