def repetidos(lista):
    lista3 = []
    for i in range(len(lista)-1):
        lista1 = list(zip(lista[i:i+1], lista[i+1:i+2]))
        if lista1[0][0] == lista1[0][1]:
            lista2 = [j for j in lista1[0]]
            list.append(lista3, lista2[0])
    n = len(lista3)
    return n