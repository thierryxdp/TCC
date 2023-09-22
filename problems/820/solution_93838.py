def posLetra(frase:str,letra:str,ocorrencia:int)->int:
    """Dada uma frase, uma letra e a ocorrência da letra na frase, retorna a posição da ocorrência na frase. Caso tenha menos ocorrências que a indicada, retorna -1."""
    proximo=0
    posicao=[]
    if str.count(frase,letra)<ocorrencia:
        return -1
    while proximo<len(frase):
        if frase[proximo]==letra:
            list.append(posicao,proximo)
        proximo=proximo+1
    return posicao[ocorrencia-1]