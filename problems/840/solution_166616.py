def bolos(A,B,C):
    """função que retorna a quantidade máxima de bolos que se pode fazer com base na receita dados A xícaras de farinha de trigo, B ovos e C colheres de sopa de leite"""
    return gcd(A//2,B//3,C//5)