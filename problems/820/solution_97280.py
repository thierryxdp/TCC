def posLetra(frase:str,letra:str,ocorrencia:int) -> int:
    """Dada uma frase, uma letra e um número que
    indica a ocorrência desejada da letra,a função
    retorna a posição da ocorrência desejada na string.
    Caso não haja a ocorrência pedida, será retornado -1."""
    
    i = 0
    posicoes = list()
    resposta = 0
    
    while i < len(frase):
        if frase[i] == letra:
            list.append(posicoes,i)
        i+=1
    if len(posicoes) < ocorrencia:
        resposta = -1
    else:
        resposta = posicoes[ocorrencia-1]
    
    return resposta