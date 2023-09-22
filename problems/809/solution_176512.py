def intercala(lista1, lista2):
    """função que intercala lista1 e lista2 e retorna uma terceira lista"""
    "lista1,lista2->lista3"
    lista3 = [ ]
    for i in range (0,len(lista1)):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
        return L3