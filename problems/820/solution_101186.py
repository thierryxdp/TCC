def posLetra(frase,letra,ocorrencia):
    """Funcao que retorna a posicao da ocorrencia de uma letra
    str, str, int --> int"""
    i = 0
    posicao = 0
    if str.count(frase,letra) < ocorrencia:
        return -1
    while i < ocorrencia:
        if ocorrencia < 2:
            x = str.find(frase,letra)
            posicao = posicao + x 
            i +=1
        if ocorrencia < 3:
            x = str.find(frase,letra,str.find(frase,letra)+1)
            posicao = posicao + x - str.find(frase,letra)
            i +=2
        if ocorrencia < 4:
            x = str.find(frase,letra,str.find(frase,letra,0,2)+1)
            posicao = posicao + x 
            i +=3
    return posicao