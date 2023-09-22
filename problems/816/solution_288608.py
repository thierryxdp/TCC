def maiores(lista_numero,n):
    'retorna uma lista crescente com os numeros maiores que o dado'
    'lista,int----lista'
    lista_numero+=[n, ]
    lista_numero.sort()
    indice=lista_numero[n]
    lista=lista_numero[indice+1:]
    return lista