def media_matriz(M):
    '''Recebe uma matriz de inteiros não vazia e retorna a média de todos os inteiros com aproximação de 2 casas decimais;
    list -> float'''
    soma = 0
    total = 0
    for i in range(len(M)):
        for j in range(len(M[i])):
            soma = soma + M[i][j]
            total = total + 1
    media = soma/total
        
    return round(media,2)