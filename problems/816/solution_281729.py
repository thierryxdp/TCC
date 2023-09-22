def maiores(lista_numero, n):
     
    lista=lista_numero+[n]
    lista_nova=list.pop(lista,lista[0]<n)
    return list.sort(lista_nova)