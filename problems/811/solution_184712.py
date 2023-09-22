def colchao(medidas,h,l):
    '''função que retorna se João consegue um colchão de 
    dimensões A, B e C, pela porta de sua casa, que tem 
    altura h e largura l
    list[A,B,C], int, int -> bool'''
    list.sort(medidas)
    if medidas[1] < max(h,l) and medidas[0] < min(h,l):
        return True
    else:
        return False