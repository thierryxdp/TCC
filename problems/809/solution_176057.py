def intercala(lista1, lista2):  
    """Cria uma lista vazia L3,
    adiciona o primeiro elemento da lista L1, depois o primeiro da lista L2
    e repete o processo com o segundo e terceiro elemento.
    lista, lista-> lista
    """
    L3=[]
    L3+=L1[0]+L2[0]+L1[1]+L2[1]+L1[2]+L2[2]
    return L3