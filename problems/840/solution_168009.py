def bolos(a,b,c):
    """calcula quantos bolos serão feitos com a quantidade dada de trigo(a),ovos(b), leite(c)
    Entrada: int
    Saída: int"""
    a//2= a, b//3= b, c//5= c
    return min(a,b,c)