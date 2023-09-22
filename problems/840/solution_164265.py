# Dadas as quantidades a, b e c de farinha, ovos e leite, esta função retorna
#a quantidade de bolos que é possível fazer com a receita do enunciado.
def bolos(a,b,c):
    return min(a//2,b//3,c//5)