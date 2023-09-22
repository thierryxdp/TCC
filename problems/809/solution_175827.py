# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    x = list(lista1)
    y = list(lista2)
    x0 = lista1[0]
    x1 = lista1[1]
    x2 = lista1[2]
    y0 = lista2[0]
    y1 = lista2[1]
    y2 = lista2[2]
    
    z = str(x0) + str(y0) + str(x1) + str(y1) + str(x2) + str(y2)
    return list(z)
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""