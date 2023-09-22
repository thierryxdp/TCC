def filtraMultiplos (Lista, n):
    i = 0
    lista_nova = []
    while i < len(lista):
        if lista[i]%n == 0:
            lista_nova+=(lista[i],)
        i+=1
    return lista_nova