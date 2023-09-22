def soma(mat):
    """dco"""
    soma_ = 0
    for linha in mat:
        for elem in linha:
            soma_ += elem
    return soma_

def melhor_volta(tempos):
    """doc"""
    menor = soma(tempos)
    melhor = []
    for i in range(len(tempos)):
        for j in range(len(tempos[i])):
            if tempos[i][j] < menor:
                menor = tempos[i][j]
                melhor = i+1, tempos[i][j], j+1
    return tuple(melhor)