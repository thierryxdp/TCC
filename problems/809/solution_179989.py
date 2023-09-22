def intercala(lista1, lista2):
    interl1impar = lista1[0::2]
    interl1par = lista1[1::2]
    interl2impar = lista2[0::2]
    interl2par = lista2[1::2]
    lista_resul = interl1impar + interl2impar + interl1par + interl2par
    return lista_resul