def intercala(lista1, lista2):
    lista=[]
    lista3=[lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]]
    for i in lista3:
        lista.append(i)
    return list(lista3)