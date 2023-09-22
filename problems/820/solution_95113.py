def posLetra(string,letra,n):
    '''A função recebe uma string, uma letra e um número n que indica a ocorrência
    desejada da letra. A função retorna em que posição da string aquela ocorrência da letra
    está. Caso exista menos ocorrências da letra do que a ocorrência n, a função retorna -1
    Parâmetros de entrada: str, str, int
    Valor de retorno: int'''
    ocorrencia=0
    pos=0
    while ocorrencia<n:
        if letra==string[pos]:
            ocorrencia=ocorrencia+1
        pos=pos+1
        if pos==len(string) and ocorrencia<n:
            return -1
    return pos-1