def faltante(lista):
    lista2 = []
    for i in lista:
        lista2.append(i)
    lista2.sort()
    ultimo= len(lista2)
    lista3 = []
    for j in range(1,lista2[ultimo-1]):
        lista3.append(j)
    for i in lista2:
        for j in lista3:
            if lista2[i] != lista3[j]:
                return lista3[i]