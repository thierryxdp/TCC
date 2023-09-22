def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    resultado = []
    index = 0
    n_da_lista1 = 0
    n_da_lista2 = 0
    while index < 6:
        if index % 2 == 0:
        	resultado.append(lista1[n_da_lista1])
        	n_da_lista1 +=1
        else:
            resultado.append(lista2[n_da_lista2])
            n_da_lista2 +=1
        index += 1
    return resultado