def intercala(lista1, lista2):
    """Função que, dadado duas listas, retorna a concatenação das mesmas"""
    '''list,list--->list'''
    return lista1[::2] + lista2[::2]