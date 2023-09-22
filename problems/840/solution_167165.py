def bolos(a,b,c):
    """Será feita a divisão dos valores com seus pesos
    para encontrar a quantidade máxima inteira de bolos que
    podem ser feitos, e então o menor valor entre os 3 será o
    número de bolos"""
    return min(a//2,b//3,c//5)