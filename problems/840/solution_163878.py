def bolos(A,B,C):
    """Calcula a quantidade de bolos que pode ser feita dados
        a quantidade de xicaras de farinha (A)(2 por bolo),
        quantidade de ovos (B)(3 por bolo) e a
        quantidade de colheres de sopa de leite (C)(5 por bolo)"""
    return min(A//2,B//3,C//5)