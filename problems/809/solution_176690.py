def intercala(lista1, lista2):
    """Função que, dado duas listas, retorna a concatenação alternada das mesmas"""
    lista3 = lista1[0:-1:2] + lista2[0:-1:2]
    return