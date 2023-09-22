def maiores(lista_num,n):
    lista=lista_num+[n]
    list.sort(lista)
    list.remove(lista,lista[:n])
    list.remove(lista,n)
    return lista