def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    resultado = []
    index = 0
    for n in lista1:
        if index % 2 == 0:
        	resultado[index] = lista1[index]
        else:
            resultado[index] = lista2[index]
        index += 1
    return resultado