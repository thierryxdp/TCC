def bolos(A,B,C):
    '''recebe determinada quantidade de ingrdientes (farinha,ovos e leite) e ve quantos bolos da pra fazer com essa quantidade de ingredientes
    int,int,int->int'''
    total_farinha= A%2
    total_ovos= B%3
    total_leite= C%5
    total_bolos= min(total_farinha,total_ovos,total_leite)
    return total_bolos