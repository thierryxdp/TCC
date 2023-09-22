def eh_quadrada(matriz):
    'Função que recebe uma matriz e analisa se ela é quadrada ou não.'
    'list->bool'

    x=len(matriz)

    if x==0:
        return True
    else:
        y=len(matriz[0])
    if x==y:
        return True
    else:
        return False