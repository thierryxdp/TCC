def intercala(lista1, lista2):
    """Retorna uma lista intercalando os elementos
    da lista1 e lista2 ambas de tamanho 3 que foram
    passadas como parametro.
    list,list-> list"""
    l1 = lista1
    l2 = lista2
    lista3 = [l1[0],l2[0],l1[1],l2[1],l1[2],l2[2]]
    return lista3