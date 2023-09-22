def bolos(a,b,c):
    '''calcula a quantidade maxima de bolos que Joao pode fazer, dados a quantidade de xicaras de farinha de trigo a, a quantidade de ovo b e a quantidade de colheres de sopa de leite c;
       int, int, int -> int'''
    return min(a//2,b//3,c//5)