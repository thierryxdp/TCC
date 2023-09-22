def insere(lista,n):
    z=0
    for x in lista:
        z+=1
        if n >x:
            lista.insert(z,n)
            break
    return lista