def bolos (A,B,C):
    """Calcula e retorna a quantidade máxima de bolos que se pode fazer com as seguintes entradas: o número de xícaras de farinha de trigo(A), o número de ovos(B) e o número de colheres de sopa de leite (C)"""
    if A<2, B<3, C<5:
        return 0
    else:
         return max(A//2,B//3,C//5)