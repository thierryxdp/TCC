def maiores(lista,n):
    lista = lista.append(n)
    lista = lista.sort(reverse = True)
    sub_lista = [ elem for elem in lista if elem > n ]
    return sub_lista