def faltante(lista):
    listaPecasEsperadas =[]
    for i in range(1, len(lista)+2):
        if (i not in lista):
            return i