def faltante(lista):
    lista2 = []
    for i in lista:
        lista2.append(i)
    lista2.sort()
    ultimo= len(lista2)
    lista3 = []
    for j in range(1,lista2[ultimo-1]):
        lista3.append(j)
    for i in lista3:
        for j in lista2:
            if lista3[i] != lista2[j]:
                return lista3[i]