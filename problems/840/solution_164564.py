def bolos (a,b,c):
    '''função que retorna a quantidade máxima possível de bolos que
    João pode fazer, dados a quantidade de xícaras  de farinha de 
    trigo (a), a quantidade de ovos (b) e a quantidade de colheres
    de sopa de leite (c), tal que a quantidade de ingredientes
    (a,b,c) sejam igualmente múltiplas de (a=2),(b=3) e (c=5);
    int,int,int->int'''
    return ((a+b+c)//10)