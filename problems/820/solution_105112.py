def posLetra(string,letra,n):
    """recebe como entrada uma string,uma letra, e um numero que indica a acorrencia desejada da letra,
    retorna em que posicao da string aquela ocorrencia da letra esta"""
    n=0
    if string.count(letra)<n:
        return -1
    while n<len(string):
        if string.index(letra)==n:
            return n
        n+=1