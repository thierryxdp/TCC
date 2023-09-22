def intercala(lista1, lista2):
    """Funcao que intercala duas listas (lista1 e lista2) formando uma terceira lista
    que e o resultado da intercalacao.
    list, list -> list"""
    listA = [lista1[0],] + [lista2[0],]
    listB = [lista1[1],] + [lista2[1],]
    listC = [lista1[2],] + [lista2[2],]
    list3 = listA + listB + listC
    return lista3