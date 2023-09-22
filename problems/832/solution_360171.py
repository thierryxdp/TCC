def eh_quadrada(matriz):
    '''função que dada uma matriz retorna se ela é quadrada ou não:matriz->bool'''
    linha = len(matriz)
    elementos = len(matriz[0])
    coluna = elementos/linha
    if linha == coluna:
        return True
    else:
        return False