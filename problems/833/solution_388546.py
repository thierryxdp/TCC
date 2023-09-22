def conta_numero(N,M):
    '''Recebe um número e uma matriz de tamanho qualquer e retorna quantas vezes o número aparece;
    int, list -> int'''
    soma = 0
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == N:
                soma = soma + 1

    return soma