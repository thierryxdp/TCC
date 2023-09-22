def intercala(lista1, lista2):
    """Função que, dado duas listas, retorna a concatenação das mesmas"""
    '''list,list--->list'''
    lista3 = lista1[0::1] + lista2[0::1]
    return lista3