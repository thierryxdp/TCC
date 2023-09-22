def conta_numero (n, matriz):
    """funçao que recebe um numero n, uma matriz e retorna quantos numeros n tem na matriz;
    entrada: int, list;
    saida: int."""    
    soma = 0                     
    for i in matriz:
        for j in i:
            if j == n:
                soma += 1
    return soma