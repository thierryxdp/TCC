def bolo(A,B,C):
    """calcula e retorna a quantidade máxima de bolo que dar para fazer com A(xícars de farinha), B(ovos) e C(colheres de leite). float->int"""
    return min(A//2,B//3,C//5)