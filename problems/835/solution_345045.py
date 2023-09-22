def melhor_volta(A):
    '''recebe uma matriz 6x10, com os tempos em segundos dos corredores em cada volta e retorna uma tupla informando
    de quem foi a melhor volta da prova, com qual tempo e em que volta'''
    menorTempo = 0
    menorVolta = 0
    corredor = 0
    for i in range(len(A)):
        if A[i] == min(len(A)):
            corredor = corredor + A[i]
        for j in range(len(A[0])):
            if A[j] == min(len(A[0])):
                menorVolta = menorVolta + A[j]
            elif A[i][j] == min(len(A[0])):
                menorTempo = menorTempo + A[i][j]
    return (corredor, menorTempo, menorVolta)