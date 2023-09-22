def posLetra(string,letra,n):
    """recebe como entrada uma string,uma letra, e um numero que indica a acorrencia desejada da letra,
    retorna em que posicao da string aquela ocorrencia da letra esta"""
    m=0
    p=0

    if string.count(letra)<n:
        return -1
    else:
        while n<m:
            if p!=n:
                p=p+str.find(string[p:],letra)
        return p