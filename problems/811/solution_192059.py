def colchao(medidas, H, L):
    '''função que retorna se é verdadeiro ou falso a condição do colchão passa pela porta dados uma lista com as dimensões do colchão e da porta.int,int,int->booleano'''
    alturaColchao = medidas[1]
    larguraColchao = medidas[2]
    if alturaColchao <= H or larguraColchao <=L:
        return True
    return False