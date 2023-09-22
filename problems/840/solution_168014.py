def bolos(a,b,c):
    """calcula quantos bolos serão feitos com a quantidade dada de trigo(a),ovos(b), leite(c)
    Entrada: int
    Saída: int"""
    return min(a//2, b//3, c//5)