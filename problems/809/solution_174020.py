def intercala(lista1,lista2):
    lista3= lista1+lista2
    lista4 = lista3[0:6:3]+lista3[1:6:3]+lista3[2:6:3]
    return lista4