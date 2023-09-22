def melhor_volta(M):
    """coment"""
    tupla=(0,M[0][0],0)
    for i in range(6):
        for j in range(10):
            if M[i][j]<tupla[1]:
                tupla = (i+1,M[i][j],j+1)
    return tupla