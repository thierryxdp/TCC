def bolos(A,B,C):
    '''Função calcula a quantidade máxima de bolos que podem ser feitos
    em função da quantidade mínima de cada ingredientes, sendo (A) a 
    quantidade de xícaras de farinha, (B) a quantidade de ovos
    e (C) a quantidade de colheres de sopa de leite. As quantidades
    mínimas são: 2 xícaras de farinha de trigo, 3 ovos e 5 colheres de
    sopa de leite
    int, int, int -> int'''
    return min(A//2,B//3,C//5)