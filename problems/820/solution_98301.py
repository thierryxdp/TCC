def posLetra(string,letra,n):
    """Função que recebe como entrada uma string, uma letra e um número que indica a ocorrência desejada da letra e retorrna em que posição da string aquela ocorrência da letra está,
    str,str,int --> int"""
    i= 0
    ocorrencia = 0
    while i < len(string):
        if string[i] == letra:
            ocorrencia += 1
        if ocorrencia == n:
            return i
    i += 1
    if ocorrencia < n:
        return -1