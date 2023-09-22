def primo(N):
    '''
        recebe um numero e retorna falso se o numero nao form primo ou
        verdadeiro caso esse numero seja primo
        entrada: inteiro
        saida: string
    '''
    ocorrencia = []
    for chq in range(1, N+1):
        if N%chq == 0:
           ocorrencia = ocorrencia + [int(N/chq)]
           list.sort(ocorrencia)
    if len(ocorrencia) == 2:
        return 'true'
    else:
        return 'false'