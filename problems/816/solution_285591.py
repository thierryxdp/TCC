def maiores(lista,num):
    lista=lista+[num]
    lista.sort()
    lista=lista[lista.index(num):]
    
    return lista