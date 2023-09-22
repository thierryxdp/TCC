def posLetra(frase,letra,ocorrencia):
    """posLetra recebe como entrada uma string, uma letra, e um inteiro que
    indica a ocorrencia desejada da letra (1 para primeira ocorrencia, 2 para
    segunda, etc) e retorna em que posicao da string aquela ocorrencia da letra
    esta. Caso existam menos ocorrencias da letra do que a ocorrencia pedida,
    devolve uma mensagem.
    str, str, int -> int ou str"""
    
    i = 0
    nocs = 0
    while i<len(frase) and nocs<ocorrencia:
        if frase[i] == letra:
            nocs = nocs +1
        i = i + 1
    if nocs < ocorrencia:
        return -1 +str(nocs)+" ocorrencias de "+str(letra)
    else:
        return i-1