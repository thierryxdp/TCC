def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    lista1[1:1] = lista2[0:]
    lista1[3:3] = lista2[1:]
    lista1[-1:] = lista2[-1:]
    lista3 = lista1[0:-1]
    
    return lista3