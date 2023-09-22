def bolos(A,B,C):
    "Calcula a quantidade máxima de bolos que pode ser feita"
    return min(A//2, B//3, C//5)
#testes(4,6,10) resultado esperado 2.0 || (4,6,9) resultado 1.0