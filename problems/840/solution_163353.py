def bolos(A,B,C):
    """Pede um número inteiro de xícaras de farinha de trigo,
    ovos e colheres de sopa de leite que João tem em casa
    e calcula quantos bolos ele consegue fazer"""
    trigo=A//2
    ovos=B//3
    leite=C//5
    m=min(trigo,ovos,leite)
    return m