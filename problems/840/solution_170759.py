def bolos(A,B,C):
    """Esta funcao calcula quantos bolos, no maximo, Joao podera fazer com 3
    ingredientes, A, B e C."""
    farinha=A//2
    ovos=B//3
    leite=C//5
    ing=(farinha,ovos,leite)
    return min(ing)