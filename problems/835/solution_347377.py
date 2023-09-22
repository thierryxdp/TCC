def melhor_volta(A):
    '''Funcao que recebe uma matriz 6x10 e mostra quem fez a melhor volta'''
    tupla = (0,float('inf'),0)
    for i in range(6):
        for j in range(10):
            if A[i][j] < tupla[1]:
                tupla = (i+1,A[i][j],j+1) #de quem, tempo, qual volta
    return tupla