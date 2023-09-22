def posLetra(string,letra,n):
    """Funcao que uma string, uma letra e um numero que indica a ocorrencia desejada da letra e retorna em que posicao da string aquela ocorrencia de letra esta. str, str, int=>int"""
    x=n
    posicao=0
    while x!=0:
        posicao=posicao+str.find(string,letra,posicao)-posicao+1
        x=x-1
    return posicao-1