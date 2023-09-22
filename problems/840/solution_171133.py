def bolos(A,B,C):
    '''Calcula a quantidade máxima de bolos dadas as entradas A para farinha, B para ovos e C para colheres de leite
    int,int,int -> int'''
    
    farinha = A//2
    ovos = B//3
    leite = C//5
    
    return min(farinha,ovos,leite)