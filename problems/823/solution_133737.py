def faltante(lista):

    list.sort(lista)
    primeiro = lista[0]
    ultimo = lista[-1]
    lista_completa=list(range(primeiro,ultimo+1))
    
    n_faltante=1
    contador = 0
    
    while contador < len(lista_completa):
        if lista_completa[contador] not in lista:
            n_faltante = lista_completa[contador]
        contador=contador+1
    return n_faltante