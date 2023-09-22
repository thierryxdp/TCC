def eh_quadrada(matriz):
    '''Funcao que identifica se uma dada matriz de entrada e ou nao quadrada,
tendo 'true' ou 'false' como retorno.
list -> bool'''
    if matriz == []:
        return True
    lin = len(matriz)
    col = len(matriz[0])
    if lin == col:
        return True
    else:
        return False