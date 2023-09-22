def bolos (A,B,C):
    ''' Funcao que retorna a quantidade maxima de bolos dado um numero de 
    xicaras de farinha de trigo (A), ovos (B) e colheres de sopa de leite
    (C). Obs: o valor minimo de ingredientes de A,B,C para fazer uma 
    unidade de bolo são 2,3,5, respectivamente.  '''
    return min(A//2,B//3,C//5)