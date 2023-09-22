def posLetra(frase,letra,n):
    """funcao, que recebe uma string, uma letra e um numero n que indica a ocorrencia desejada da letra. Retorna em que posicao da string a ocorrencia da letra dada por n esta. se nao houver tantas ocorrencias quanto a informada, retorna -1
    str,str,int--->int"""
    i=0
    while i<len(frase):
        frase=str.find(frase,letra)
    return frase