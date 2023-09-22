def melhor_volta(A):
    '''recebe uma matriz 6x10, com os tempos em segundos dos corredores em cada volta e retorna uma tupla informando
    de quem foi a melhor volta da prova, com qual tempo e em que volta'''
    menorTempo = 0
    menorVolta = 0
    for i in range(len(A)):
        if A[i] == min(len(A)):
            menorTempo = menorTempo + i
        for j in range(len(A[0])):
            if A[j] == min(len(A[0])):
            	menorVolta = menorVolta + j
    return (menorTempo, menorVolta)