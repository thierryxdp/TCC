def posLetra(string,letra,n):
    """recebe como entrada uma string,uma letra, e um numero que indica a acorrencia desejada da letra,
    retorna em que posicao da string aquela ocorrencia da letra esta"""
    m=0
    
    while m<len(string):
        if string.index(letra)==n:
            return string.find(letra,n)
        m+=1
    return -1