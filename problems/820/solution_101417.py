def posLetra(string,letra,n):
    """retorna o indice da ocorrência desejada de uma letra """
    i=0
    indice = []
    while i < len(string):
        if string[i] == letra:
            posicao = str.find(string,letra,i)
            indice = indice + [posicao,]
        i = i + 1
    if len(indice) >= n:
        return indice[n-1] 
    else: 
        return -1