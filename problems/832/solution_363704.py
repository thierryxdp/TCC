def eh_quadrada(matriz):
    ''' Função que identifica se a matriz dada como entrada é do
    tipo quadrada
    list -> bool '''

    linha = len(matriz)
    if linha == 0 or (linha*(len(matriz[0])))%2==0:
        return True
    else:
        return False