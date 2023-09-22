def maiores(lista,n):
    if n in lista:
        posicao=list.index(lista,n)
        return lista[posicao+1:]
    
    if n not in lista:
        lista.append(n)
        list.sort(lista)
        posicao=list.index(lista,n)
        return lista[posicao+1:]
    
def acima_da_media(lista):
    media=sum(lista)/len(lista)
    return maiores(lista,media)