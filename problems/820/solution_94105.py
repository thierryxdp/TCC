def posLetra(texto, letra, numero):
    '''Calcula e retorna o valor da posicao de uma letra em um texto a partir de sua ocorrencia
       parameters:
       texto: um texto qualquer
       letra: uma letra presente no texto
       numero: a ocorrencia dessa letra no texto
    str,str,int->int'''
    proximo=0
    posicao=[]
    if texto.count(letra) < numero:
        return -1
    while proximo < len(texto):
        if texto[proximo] == letra:
            posicao.append(proximo)
        proximo=proximo+1
    return posicao[numero-1]