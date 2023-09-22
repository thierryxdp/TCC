def posLetra(frase,letra,ocorrencia):
    """Funcao que retorna a posicao da ocorrencia de uma letra
    str, str, int --> int"""
    i = 0
    posicao = 0
    while i < ocorrencia:
        x = str.find(frase,letra,str.find(frase,letra)+1)
        posicao = posicao + x - 1
        i +=1
    return posicao