def bolos(a,b,c):
    """calcula quantos bolos serão feitos com a quantidade dada de trigo(a),ovos(b), leite(c)
    Entrada: int
    Saída: int"""
    a== a//2, b== b//3, c== c//5
    return min(a,b,c)