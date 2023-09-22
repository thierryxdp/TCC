def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    lista = lista1
    lista.insert((1,3,5), int(lista2))
    return lista