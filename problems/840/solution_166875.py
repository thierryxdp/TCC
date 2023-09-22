def bolos (A, B, C):
    """ calcula a quantidade de bolos dado as quantidades dos
    elementos A, B e C e retorna o menor valor """
    A//2
    B//3
    C//5 
    if A < 2:
        print (0)
    if B < 3:
        print (0)
    if C < 5:
        print (0)
    return min (A//2, B//3, C//5)