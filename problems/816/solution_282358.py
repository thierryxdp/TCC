def maiores(lista,n):
    list.insert(lista,1,n)
    lista.sort()
    lista=str(lista)
    lista=lista.strip('[]')
    posicao=str.find(lista,str(n))
    
    
    
    return posicao