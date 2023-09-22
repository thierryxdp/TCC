def melhor_volta(M):
    """Dada uma matriz 6x10 com 6 corredores e 10 voltas, a função retorna
    uma tupla contendo a melhor volta, qual o tempo da melhor volta, quem
    foi o dono da melhor volta, tendo em vista que os corredores são 
    representados de 1 a 6 e as corridas de 1 a 10;
    list(list(float))->tuple(int,float,int)"""
    tupla=(0,M[0][0],0)
    for i in range(6):
        for j in range(10):
            if M[i][j]<tupla[1]:
                tupla = (i+1,M[i][j],j+1)
    return tupla