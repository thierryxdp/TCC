def posLetra(frase,letra,ocorrencia):
    '''Recebe uma frase, uma letra e a ocorrência desejada dessa letra na
    frase e retorna o índice dessa ocorrência. (str,str,int -> int)'''
    ocorrencias = []
    proximo = 0 
    while proximo < len(frase):
        if letra in frase[proximo]:
            ocorrencias = ocorrencias + [frase[proximo],]
        proximo = proximo + 1
    if len(ocorrencias) <= ocorrencia:
        return ocorrencias[ocorrencia - 1]
    else:
        return -1