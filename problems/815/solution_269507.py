def insere(lista,n):
    z=0
    teste = False
    for x in lista:
        z+=1
        if n <x:
            teste = True
            lista.insert(z-1,n)
            break
    if teste == False:
        lista.append(n)
    return lista