def posLetra(frase,letra,n):
    '''Recebe como entrada uma frase(str), uma letra(str), e um número(int) que indica a ocorrência desejada da letra
    e retorna em que posição da string aquela ocorrência da letra está(int).'''
    if frase.count(letra) < n:
        return -1
    x=0
    ocorrencia=0
    while x < len(frase):
        if letra in frase:
            ocorrencia=ocorrencia+1
            if ocorrencia == n:
                return frase.index(letra, n)
        x=x+1