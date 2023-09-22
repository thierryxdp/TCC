def insere(lista_numero,n):
    for i in range(-1,len(lista_numero)):
        j = i
    while j>=1 and lista_numero[j-1]>lista_numero[j]:
        lista_numero[j-1],lista_numero[j] = lista_numero[j],lista_numero[j-1]
        j = j-1
    return lista_numero