def bolos (a,b,c):
    '''função que retorna a quantidade máxima possível de bolos que
    João pode fazer, dados a quantidade de xícaras  de farinha de 
    trigo (a), a quantidade de ovos (b) e a quantidade de colheres
    de sopa de leite (c), tal que a quantidade de ingredientes seja:
    (a) múltiplo de 2,(b) múltiplo de 3,(c) múltiplo de 5;
    int,int,int->int'''
    return max((a//2),(b//3),(c//5))