def melhor_volta(matriz):
    """determina qual o vencedor de uma corrida e seus resultados;
    matriz, -> tupla"""
    m = matriz
    a1 = sum(m[0])
    a2 = sum(m[1])
    a3 = sum(m[2])
    a4 = sum(m[3])
    a5 = sum(m[4])
    a6 = sum(m[5])
    b = min(a1,a2,a3,a4,a5,a6)
    
    return b/10