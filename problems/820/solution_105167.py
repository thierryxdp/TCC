def posLetra(string,letra,n):
    """recebe como entrada uma string,uma letra, e um numero que indica a acorrencia desejada da letra,
    retorna em que posicao da string aquela ocorrencia da letra esta"""
    m=1
    if string.count(letra)<n:
        return -1
    else:
        while str.find(string,letra,m)!=n:
            m+=1
        return m