def eh_quadrada(matriz):
    ''' Função que identifica se a matriz dada como entrada é do
    tipo quadrada
    list -> bool '''

    linha = len(matriz)
    coluna = len(matriz[0])
    if linha == coluna or (linha*coluna) == 0 or len(matriz) == 0:
        return True
    else:
        return False