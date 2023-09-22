def intercala(L,L2):
    intercalada = []
    for a,b in zip(L, L2):
        intercalada.append(a)
        intercalada.append(b)
    return intercalada

lista1 = [1,2,3]
lista2 = [4,5,6]

listaIntercalada = intercala(lista1, lista2)