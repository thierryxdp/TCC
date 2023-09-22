def colchao(medidas,h,l):
    '''função que retorna se João consegue um colchão de 
    dimensões A, B e C, pela porta de sua casa, que tem 
    altura h e largura l
    list[A,B,C], int, int -> bool'''
    list.sort(medidas)
    if medidas[2] > max(h,l)
        return False
    elif medidas[1] > min(h,l)
        return False
    else:
        return True