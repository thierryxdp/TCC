def bolos(A, B, C):
    """Computa a quantidade máxima de bolos
    possíveis a partir dos ingredientes A, B, C,
    podendo desperdiçar o que sobra.
    
    Cada bolo requer 2A, 3B e 5C.  Se tivermos
    muito B ou C e pouco A, então só conseguimos o
    número de bolos que A nos permite, ou seja, o
    mais escassos dos ingredientes é quem determina
    a quantidade de bolos.
    """
    return min(A//2, B//3, C//5)