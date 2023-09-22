def posLetra(frase:str,letra:str,ocorrencia:int)->int:
    """Dada uma frase, uma letra e a ocorrência da letra na frase, retorna a posição da ocorrência na frase. Caso tenha menos ocorrências que a indicada, retorna -1."""
    proximo=0
    if str.count(frase,letra)<ocorrencia:
        return -1
    while proximo<len(frase) or ocorrencia!=0:
        if frase[proximo]==letra:
            ocorrencia=ocorrencia-1
        posicao=str.index(frase,letra,frase[proximo]+1,len[frase])
        proximo=proximo+1
    return posicao