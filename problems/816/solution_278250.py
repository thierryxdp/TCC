def maiores(lista,n):
    lista=lista.sort()
    lista =lista[:] - lista[n:]
    
    return lista