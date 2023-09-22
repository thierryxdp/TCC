def intercala(lista1, lista2):
    Lista3 = [ ]
    for i in range(0, len(lista1)):
        Lista3.append(lista1[i])
        Lista3.append(lista2[i])
        for j in range(1, len(lista1)):
        Lista3.append(lista1[j])
        Lista3.append(lista2[j])
        return Lista3