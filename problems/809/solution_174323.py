def intercala(lista1,lista2):
    "intercala duas listas com três números cada"
    lista3=lista1+lista2
    lista3[::2]=lista1
    lista3[1::2]=lista2
    return lista3