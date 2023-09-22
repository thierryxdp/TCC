def bolos(A,B,C):
    """calcula a quantidade de bolos podem ser feitos
com os devidos ingredientes dados
A(farinha de trigo), B(ovo), C(colheres de sopa de leite)"""
    if (A,B,C) >= (2,3,5):
        return ((A//2)+(B//3)+(C//5))//3
    else:
        return "Não tem ingrediente suficiente"