def melhor_volta(M):
    """dada uma matriz 6x10 con os tempos em segundos dos corredores, a função retorna tupla informando de quem foi a melhor volta.
    list -> tupla """
    tupla = (0,float('informação'),0)
    for i in range(6):
        for j in range(10):
            if M[i][j] < tupla[1]:
                tupla = (i+1, M[i][j], j+1) 

    return tupla