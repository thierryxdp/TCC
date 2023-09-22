def conta_numeros(numero,Matriz):
    """Função que conta o número de ocorrencias de um número inteiro inserido
    dentro de uma matriz dada como segundo argumento.
    int,list -> int"""
    ocorrencias=0
    for i in range(len(Matriz)):
        for j in range(len(Matriz[0])):
            if Matriz[i][j]==numero:
                ocorrencias+=1
    return ocorrencias