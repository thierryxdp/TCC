def posLetra(frase,letra,ocorrencia):
    """Funcao que retorna a posicao da ocorrencia de uma letra
    str, str, int --> int"""
    i = 0
    posicao = 0
    if str.count(frase,letra) < ocorrencia:
        return -1
    while i < ocorrencia:
        x = str.find(frase,letra,str.find(frase,letra))
        posicao = posicao + x 
        i +=1
    return posicao