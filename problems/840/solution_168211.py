def bolos(A,B,C):
    '''calcule a quantidade de bolo que possivel fazer,
    dado a quantidade de ingredientes de entrada:
    xicaras de farinha (A) ovos(8),colheres de sopa de leite (C).
    int,int,int -> int'''
    if(A//2) and (8//3) and (C//5) >=1:
        return min((A//2),(3//3), (C//5))
    else:
        return 0