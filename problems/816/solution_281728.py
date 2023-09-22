def maiores(lista_numero, n):
     
    lista=lista_numero+[n]
    lista_nova=list.pop(lista,lista[0]<n)
    return sorted(lista_nova)