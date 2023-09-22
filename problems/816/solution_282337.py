def maiores(lista,n):
    list.insert(lista,1,n)
    lista.sort()
    lista=str(lista)
    posicao=str.find(lista,str(n))
    return list(lista[(int(posicao+1)):])