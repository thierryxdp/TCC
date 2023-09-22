def insere(lista,n):
    z=-1
    for x in lista:
        z+=1
        if n > x:
            lista.insert(z,n)
    return lista