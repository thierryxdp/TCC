def posLetra(string,letra,n):
    ''' função que recebe como entrada uma string, uma letra, e um número que indica a ocorrência desejada da letra e retornar em que posição da string aquela ocorrência da letra está. 
    Entrada: str, str, int
    Saída: int'''
    acumulador = 0
    proximo = 0
    while acumulador < n and proximo < len(string):
        if string[proximo] == letra:
            acumulador = acumulador + 1
        proximo = proximo + 1
    if acumulador == n:
        return proximo -1
    elif acumulador < n:
        return -1