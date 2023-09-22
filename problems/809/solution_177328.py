def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    lista3 = list()
    lista1 = [0,1,2]
    lista2 = [0,1,2]
    for a,b in zip(lista1,lista2):
        lista3.append(a)
        lista3.append(b)
        return lista3