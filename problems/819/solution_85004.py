def filtraMultiplos (Lista, n):
    i = 0
    lista_nova = []
    while i < len(Lista):
        if Lista[i]%n == 0:
            lista_nova+=(Lista[i],)
        i+=1
    return lista_nova