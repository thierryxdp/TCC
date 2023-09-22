def bolos(A, B, C):
    """Calcula a quantidade máxima de bolos feitos a 
    partir da quantidade de ingredientes disponíveis,
    sendo A:=xícaras; B:=ovos; C:colheres de leite. 
    1 bolo requer 2A + 3B + 5C"""
    return min(A//2, B//3, C//5)