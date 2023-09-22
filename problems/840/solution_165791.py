def bolos(A,B,C):
    '''Função que calcula a quantidade máxima de bolos que
    pode ser feita com A xícaras de farinha, B ovos e C 
    colheres de sopa de leite.
    int,int,int->int'''
    farinha=A//2
    ovos=B//3
    leite=C//5
    return min(farinha,ovos,leite)