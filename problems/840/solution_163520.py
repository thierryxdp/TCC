def bolo(A,B,C):
    """calcula a quantidade de bolos podem ser feitos
com os devidos ingredientes dados
A(farinha de trigo), B(ovo), C(colheres de sopa de leite)"""
    return min(A//2,B//3,C//5)