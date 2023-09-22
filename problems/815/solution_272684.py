def insere(lista_numero,n):
    for i in range(1,len(lista_numero)):
        j = i
    while j>=1 and L[j-1]>L[j]:
        L[j-1],L[j] = L[j],L[j-1]
        j = j-1
    return L