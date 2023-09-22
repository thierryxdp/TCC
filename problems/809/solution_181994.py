def intercala(lista1, lista2):
    """Dadas duas listas (1 e 2) como entradas, retorna outra lista com os 
    valores intercalados presentes nelas, iniciando com o primeiro
    valor da lista um e terminando com o último valor da lista dois.
    list, list --> list"""
    listaX = ['','','','','','']
    listaX[0::2] = lista1
    listaX[1::2] = lista2
    return listaX