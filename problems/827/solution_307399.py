def qtd_divisores(N):
    '''
        recebe um numero intero e retorna a quantidade de divisores que ele tem
        entrada: inteiro
        saida: inteiro
    '''
    total_div = 1
    ocorrencia = [1]
    for chq in range(1, N):
        if N == 1:
            return total_div
        if N < 0:
            return 0
        if N%chq == 0:
           total_div = total_div + 1
           ocorrencia = ocorrencia + [int(N/chq)]
           list.sort(ocorrencia)
    return total_div