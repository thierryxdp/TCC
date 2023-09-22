#list(int)->int
def media_matriz(Matriz):
    S = [0]*len(Matriz)
    for i in range(0,len(Matriz)):
        soma_linhas = 0
        for j in range(0,len(Matriz[0])):
            soma_linhas += Matriz[i][j]
        S[i] = soma_linhas
    return round(S/len(Matriz(,2)