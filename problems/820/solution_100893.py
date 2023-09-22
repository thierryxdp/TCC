def posLetra(frase, letra, ocorrencias):
    """A funcao indica a posicaoda letra pedida.
    str,str,int--->int"""
    posicao=0
    contagem=0
    while len(frase) > posicao and contagem < ocorrencia:
        if frase[posicao] == letra:
            contagem = contagem+1
        posicao = posicao+1
    if contagem < ocorrencia:
        return -1
    else:
        return posicao - 1