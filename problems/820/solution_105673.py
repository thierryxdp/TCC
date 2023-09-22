def posLetra(frase,letra,ocorrencia):
    '''Recebe uma frase, uma letra e a ocorrência desejada dessa letra na
    frase e retorna o índice dessa ocorrência. (str,str,int -> int)'''
    ocorrencias = 0
    proximo = 0 
    while proximo < len(frase):
        if letra == frase[proximo]:
            ocorrencias = ocorrencias + 1
        proximo = (proximo + 1)
        if len(ocorrencias) < ocorrencia:
            return ocorrencias[ocorrencia - 1]
        else:
            return -1