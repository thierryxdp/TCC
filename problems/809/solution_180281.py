def intercala(lista1, lista2):
    """função que dada duas(lista1 e lista2) list de tamanho 3 retorna uma nova list que contem lista1 e lista2 intercaladas;list->list"""
    lista3=lista1[:1]+lista2[:1]
    lista4=lista1[-2:-1]+lista2[-2:-1]
    lista5=lista1[-1:]+lista2[-1:]
    lista7=lista3+lista4+lista5
    return lista7