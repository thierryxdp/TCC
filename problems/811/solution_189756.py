def colchao(medidas, H, L):
    ''' Esta função compara os valores de índice [1] e [2] de
    uma lista chamada 'medidas' com os valores H e L
    respectivamente.
    list, int, int->bool'''
    if medidas[1] <= H or medidas[2] <= L:
        return True